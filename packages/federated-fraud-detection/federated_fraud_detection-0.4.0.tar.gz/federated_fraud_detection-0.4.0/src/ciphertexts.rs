use std::ops::{BitXor, BitXorAssign};

use curve25519_dalek::{ristretto::{RistrettoBasepointTable, RistrettoPoint, CompressedRistretto}, scalar::Scalar, constants::RISTRETTO_BASEPOINT_TABLE};
use okvs::bits::Bits;
use rand::thread_rng;

use crate::wide_ciphertexts::WideCiphertext;

#[derive(Debug, Clone, Copy)]
pub struct Ciphertext {
    c1: [u8; 32],
    c2: [u8; 32],
}

impl Ciphertext {
    pub fn zero(public_key_table: &RistrettoBasepointTable) -> Self {
        let randomness = Scalar::random(&mut thread_rng());

        Self {
            c1: (&randomness * &RISTRETTO_BASEPOINT_TABLE).compress().to_bytes(),
            c2: (&randomness * public_key_table).compress().to_bytes(),
        }
    }

    pub fn add_and_randomize(ciphertext_a: Self, ciphertext_b: Self, public_key: &RistrettoPoint) -> WideCiphertext {
        let randomness = Scalar::random(&mut thread_rng());

        let point_a_c1 = CompressedRistretto::from_slice(&ciphertext_a.c1).decompress().expect("C1 of ciphertext A was not a valid curve point.");
        let point_a_c2 = CompressedRistretto::from_slice(&ciphertext_a.c2).decompress().expect("C2 of ciphertext A was not a valid curve point.");
        let point_b_c1 = CompressedRistretto::from_slice(&ciphertext_b.c1).decompress().expect("C1 of ciphertext B was not a valid curve point.");
        let point_b_c2 = CompressedRistretto::from_slice(&ciphertext_b.c2).decompress().expect("C2 of ciphertext B was not a valid curve point.");

        // Represents the sum of the two ciphertexts multiplied by some random scalar.
        WideCiphertext {
            a: (&randomness * &point_a_c1).compress().to_bytes(),
            b: (&randomness * &point_b_c1).compress().to_bytes(),
            c: (&randomness * &RISTRETTO_BASEPOINT_TABLE).compress().to_bytes(),
            d: (&randomness * &(point_a_c2 + point_b_c2 + public_key)).compress().to_bytes(),
        }
    }
}

impl Bits for Ciphertext {
    fn random() -> Self {
        // TODO: This can be done cheaper by generating random bytes and masking a bit.
        Self {
            c1: RistrettoPoint::random(&mut thread_rng()).compress().to_bytes(),
            c2: RistrettoPoint::random(&mut thread_rng()).compress().to_bytes(),
        }
    }

    const BYTES: usize = 64;

    fn to_bytes(self) -> Vec<u8> {
        [self.c1, self.c2].concat()
    }

    fn from_bytes(bytes: &[u8]) -> Self {
        let mut c1 = [0; 32];
        let mut c2 = [0; 32];

        c1.copy_from_slice(&bytes[0..32]);
        c2.copy_from_slice(&bytes[32..64]);

        Self {
            c1,
            c2,
        }
    }
}

impl BitXor for Ciphertext {
    type Output = Self;

    fn bitxor(self, rhs: Self) -> Self::Output {
        Self {
            c1: self.c1.zip(rhs.c1).map(|(x, y)| x ^ y),
            c2: self.c2.zip(rhs.c2).map(|(x, y)| x ^ y),
        }
    }
}

impl BitXorAssign for Ciphertext {
    fn bitxor_assign(&mut self, rhs: Self) {
        *self = *self ^ rhs;
    }
}
