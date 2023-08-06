use curve25519_dalek::{scalar::Scalar, ristretto::CompressedRistretto};
use rand::thread_rng;

/// Contains c1 for parties A and B as c1a and c1b. This enables the final decryption.
pub struct WideCiphertext {
    pub a: [u8; 32],
    pub b: [u8; 32],
    pub c: [u8; 32],
    pub d: [u8; 32],
}

impl WideCiphertext {
    pub fn randomize(self) -> Self {
        let randomness = Scalar::random(&mut thread_rng());

        Self {
            a: (&randomness * &CompressedRistretto::from_slice(&self.a).decompress().unwrap()).compress().to_bytes(),
            b: (&randomness * &CompressedRistretto::from_slice(&self.b).decompress().unwrap()).compress().to_bytes(),
            c: (&randomness * &CompressedRistretto::from_slice(&self.c).decompress().unwrap()).compress().to_bytes(),
            d: (&randomness * &CompressedRistretto::from_slice(&self.d).decompress().unwrap()).compress().to_bytes(),
        }
    }

    pub fn sum(self, rhs: Self) -> Self {
        Self {
            a: (CompressedRistretto::from_slice(&self.a).decompress().unwrap() + CompressedRistretto::from_slice(&rhs.a).decompress().unwrap()).compress().to_bytes(),
            b: (CompressedRistretto::from_slice(&self.b).decompress().unwrap() + CompressedRistretto::from_slice(&rhs.b).decompress().unwrap()).compress().to_bytes(),
            c: (CompressedRistretto::from_slice(&self.c).decompress().unwrap() + CompressedRistretto::from_slice(&rhs.c).decompress().unwrap()).compress().to_bytes(),
            d: (CompressedRistretto::from_slice(&self.d).decompress().unwrap() + CompressedRistretto::from_slice(&rhs.d).decompress().unwrap()).compress().to_bytes(),
        }
    }

    pub fn to_bytes(self) -> Vec<u8> {
        let mut bytes = self.a.to_vec();
        bytes.extend(self.b);
        bytes.extend(self.c);
        bytes.extend(self.d);

        bytes
    }

    pub fn from_bytes(bytes: &[u8]) -> Self {
        let mut a = [0; 32];
        let mut b = [0; 32];
        let mut c = [0; 32];
        let mut d = [0; 32];

        a.copy_from_slice(&bytes[0..32]);
        b.copy_from_slice(&bytes[32..64]);
        c.copy_from_slice(&bytes[64..96]);
        d.copy_from_slice(&bytes[96..128]);

        Self {
            a,
            b,
            c,
            d,
        }
    }
}
