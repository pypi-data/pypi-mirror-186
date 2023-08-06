#![feature(array_zip)]
mod ciphertexts;
mod data_rows;
mod point_conversion;
mod wide_ciphertexts;

use ciphertexts::Ciphertext;
use curve25519_dalek::{
    constants::ED25519_BASEPOINT_TABLE,
    edwards::{CompressedEdwardsY, EdwardsBasepointTable, EdwardsPoint},
    scalar::Scalar,
    traits::BasepointTable,
};
use data_rows::DataRow;
use okvs::schemes::{paxos::Paxos, Okvs};
use pyo3::{
    prelude::*,
    types::{PyBytes, PyTuple},
};
use rand::thread_rng;
use rayon::iter::IndexedParallelIterator;
use rayon::iter::ParallelIterator;
use rayon::{
    prelude::{IntoParallelIterator, IntoParallelRefIterator},
    slice::ParallelSlice,
};
use wide_ciphertexts::WideCiphertext;

/// Generates a key pair for this party, returning a tuple with (public_key: bytes, secret_key: bytes).
#[pyfunction]
fn key_gen(py: Python) -> &PyTuple {
    let sk = Scalar::random(&mut thread_rng());
    let pk = &sk * ED25519_BASEPOINT_TABLE;

    let pk_bytes = pk.compress().as_bytes().to_vec();
    let sk_bytes = sk.as_bytes().to_vec();

    let pk_object: PyObject = PyBytes::new(py, &pk_bytes).into();
    let sk_object: PyObject = PyBytes::new(py, &sk_bytes).into();

    PyTuple::new(py, [pk_object, sk_object])
}

fn read_public_key(py: Python, public_key: PyObject) -> EdwardsPoint {
    let public_key_bytes: &PyBytes = public_key
        .cast_as(py)
        .expect("The public key object should be of type `bytes`.");
    CompressedEdwardsY::from_slice(public_key_bytes.as_bytes())
        .decompress()
        .expect("The public key was not a valid curve point.")
}

/// Builds an OKVS for one party. Takes the public key of this party and the data from the database, which is a list of rows. Each row is a list of the relevant columns as a String.
#[pyfunction]
fn build_okvs(py: Python, public_key: PyObject, strings_in_each_row: Vec<Vec<String>>) -> PyObject {
    let public_key_table = EdwardsBasepointTable::create(&read_public_key(py, public_key));

    let data_rows: Vec<(DataRow, Ciphertext)> = strings_in_each_row
        .into_par_iter()
        .map(|row| (DataRow(row), Ciphertext::zero(&public_key_table)))
        .collect();

    // TODO: Parallelize Paxos
    let okvs: Paxos<Ciphertext> = Paxos::encode(&data_rows, 40);

    PyBytes::new(py, &okvs.to_bytes()).into()
}

#[pyfunction]
fn initiate_queries(
    py: Python,
    sender_data: Vec<Vec<String>>,
    receiver_data: Vec<Vec<String>>,
    sender_okvs: PyObject,
    receiver_okvs: PyObject,
    swift_pk: PyObject,
) -> PyObject {
    let sender_okvs_bytes: &PyBytes = sender_okvs
        .cast_as(py)
        .expect("The sender_okvs object should be of type `bytes`.");
    let sender_okvs_instance: Paxos<Ciphertext> = Paxos::from_bytes(sender_okvs_bytes.as_bytes());
    let sender_ciphertexts = sender_data
        .into_par_iter()
        .map(|row| sender_okvs_instance.decode(&DataRow(row)));

    let receiver_okvs_bytes: &PyBytes = receiver_okvs
        .cast_as(py)
        .expect("The receiver_okvs object should be of type `bytes`.");
    let receiver_okvs_instance: Paxos<Ciphertext> =
        Paxos::from_bytes(receiver_okvs_bytes.as_bytes());
    let receiver_ciphertexts = receiver_data
        .into_par_iter()
        .map(|row| receiver_okvs_instance.decode(&DataRow(row)));

    let public_key = read_public_key(py, swift_pk);
    let aggregated_ciphertexts: Vec<u8> = sender_ciphertexts
        .zip(receiver_ciphertexts)
        .flat_map(|(cs, cr)| Ciphertext::add_and_randomize(cs, cr, &public_key).to_bytes())
        .collect();

    PyBytes::new(py, &aggregated_ciphertexts).into()
}

#[pyfunction]
fn randomize(py: Python, ciphertexts: PyObject) -> PyObject {
    let ciphertexts_bytes: &PyBytes = ciphertexts
        .cast_as(py)
        .expect("The ciphertexts object should be of type `bytes`.");
    let randomized_ciphertexts: Vec<u8> = ciphertexts_bytes
        .as_bytes()
        .par_chunks(128)
        .flat_map(|chunk| WideCiphertext::from_bytes(chunk).randomize().to_bytes())
        .collect();

    PyBytes::new(py, &randomized_ciphertexts).into()
}

#[pyfunction]
fn combine(py: Python, sender_ciphertexts: PyObject, receiver_ciphertexts: PyObject) -> &PyTuple {
    let sender_ciphertexts_bytes: &PyBytes = sender_ciphertexts
        .cast_as(py)
        .expect("The sender_ciphertexts object should be of type `bytes`.");
    let receiver_ciphertexts_bytes: &PyBytes = receiver_ciphertexts
        .cast_as(py)
        .expect("The receiver_ciphertexts object should be of type `bytes`.");

    let wide_ciphertexts: Vec<WideCiphertext> = sender_ciphertexts_bytes
        .as_bytes()
        .par_chunks(128)
        .zip(receiver_ciphertexts_bytes.as_bytes().par_chunks(128))
        .map(|(x, y)| WideCiphertext::from_bytes(x).sum(WideCiphertext::from_bytes(y)))
        .collect();

    let alpha_bytes: Vec<u8> = wide_ciphertexts.par_iter().flat_map(|c| c.a).collect();
    let beta_bytes: Vec<u8> = wide_ciphertexts.par_iter().flat_map(|c| c.b).collect();
    let gamma_bytes: Vec<u8> = wide_ciphertexts.par_iter().flat_map(|c| c.c).collect();
    let delta_bytes: Vec<u8> = wide_ciphertexts.par_iter().flat_map(|c| c.d).collect();

    let sender_points: PyObject = PyBytes::new(py, &alpha_bytes).into();
    let receiver_points: PyObject = PyBytes::new(py, &beta_bytes).into();
    let gamma_points: PyObject = PyBytes::new(py, &gamma_bytes).into();
    let delta_points: PyObject = PyBytes::new(py, &delta_bytes).into();

    PyTuple::new(
        py,
        [sender_points, receiver_points, gamma_points, delta_points],
    )
}

#[pyfunction]
fn decrypt(py: Python, points: PyObject, bank_secret_key: PyObject) -> PyObject {
    let secret_key_bytes: &PyBytes = bank_secret_key
        .cast_as(py)
        .expect("The bank_secret_key object should be of type `bytes`.");
    let mut secret_key_array = [0; 32];
    secret_key_array.copy_from_slice(secret_key_bytes.as_bytes());
    let secret_key = Scalar::from_bits(secret_key_array);

    let points_bytes: &PyBytes = points
        .cast_as(py)
        .expect("The points object should be of type `bytes`.");
    let decrypted_points: Vec<u8> = points_bytes
        .as_bytes()
        .par_chunks(32)
        .flat_map(|chunk| {
            (secret_key * CompressedEdwardsY::from_slice(chunk).decompress().unwrap())
                .compress()
                .to_bytes()
        })
        .collect();

    PyBytes::new(py, &decrypted_points).into()
}

#[pyfunction]
fn finish(
    py: Python,
    sender_points: PyObject,
    receiver_points: PyObject,
    gamma_points: PyObject,
    delta_points: PyObject,
    swift_secret_key: PyObject,
) -> Vec<bool> {
    let secret_key_bytes: &PyBytes = swift_secret_key
        .cast_as(py)
        .expect("The swift_secret_key object should be of type `bytes`.");
    let mut secret_key_array = [0; 32];
    secret_key_array.copy_from_slice(secret_key_bytes.as_bytes());
    let secret_key = Scalar::from_bits(secret_key_array);

    let sender_points_bytes: &PyBytes = sender_points
        .cast_as(py)
        .expect("The points object should be of type `bytes`.");
    let receiver_points_bytes: &PyBytes = receiver_points
        .cast_as(py)
        .expect("The points object should be of type `bytes`.");
    let gamma_points_bytes: &PyBytes = gamma_points
        .cast_as(py)
        .expect("The points object should be of type `bytes`.");
    let delta_points_bytes: &PyBytes = delta_points
        .cast_as(py)
        .expect("The points object should be of type `bytes`.");

    let sender_points_iter = sender_points_bytes
        .as_bytes()
        .chunks(32)
        .map(|chunk| CompressedEdwardsY::from_slice(chunk).decompress().unwrap());
    let receiver_points_iter = receiver_points_bytes
        .as_bytes()
        .chunks(32)
        .map(|chunk| CompressedEdwardsY::from_slice(chunk).decompress().unwrap());
    let gamma_points_iter = gamma_points_bytes
        .as_bytes()
        .chunks(32)
        .map(|chunk| CompressedEdwardsY::from_slice(chunk).decompress().unwrap());
    let delta_points_iter = delta_points_bytes
        .as_bytes()
        .chunks(32)
        .map(|chunk| CompressedEdwardsY::from_slice(chunk).decompress().unwrap());

    let mut outputs = vec![];
    for (((a, b), c), d) in sender_points_iter
        .zip(receiver_points_iter)
        .zip(gamma_points_iter)
        .zip(delta_points_iter)
    {
        outputs.push(d == (a + b + secret_key * c));
    }

    outputs
}

/// A Python module for the cryptographic operations necessary to do feature extraction (element matching in two datasets).
#[pymodule]
fn federated_fraud_detection(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(key_gen, m)?)?;
    m.add_function(wrap_pyfunction!(build_okvs, m)?)?;
    m.add_function(wrap_pyfunction!(initiate_queries, m)?)?;
    m.add_function(wrap_pyfunction!(randomize, m)?)?;
    m.add_function(wrap_pyfunction!(combine, m)?)?;
    m.add_function(wrap_pyfunction!(decrypt, m)?)?;
    m.add_function(wrap_pyfunction!(finish, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use curve25519_dalek::{constants::ED25519_BASEPOINT_TABLE, scalar::Scalar};
    use rand::thread_rng;

    use crate::point_conversion::{point_to_uniform_bytes, uniform_bytes_to_point};

    #[test]
    fn test_encryption() {
        let sk = Scalar::random(&mut thread_rng());
        let pk = &sk * ED25519_BASEPOINT_TABLE;

        let (s1, s2) = loop {
            println!("loop");
            let r = Scalar::random(&mut thread_rng());

            let c1 = &r * ED25519_BASEPOINT_TABLE;
            let s1 = point_to_uniform_bytes(c1);
            if s1.is_none() {
                continue;
            }

            let c2 = &r * &pk;
            let s2 = point_to_uniform_bytes(c2);
            if s2.is_some() {
                break (s1.unwrap(), s2.unwrap());
            }
        };

        let c1 = uniform_bytes_to_point(&s1);
        let c2 = uniform_bytes_to_point(&s2);

        assert_eq!(&sk * &c1, c2);
    }
}
