use std::fs::File;
use std::io::prelude::*;
use std::io::{Error, ErrorKind};

pub fn get_dds_dimensions(file: &str) -> Result<(u32, u32), Error> {
    let mut f = File::open(file)?;
    let mut buffer = [0; 24];
    f.read_exact(&mut buffer)?;
    if [buffer[0], buffer[1], buffer[2], buffer[3]] != [0x44u8, 0x44u8, 0x53u8, 0x20u8] {
        Err(Error::new(ErrorKind::Other, "Not a DDS file!".to_string()))
    } else {
        let height = [buffer[12], buffer[13], buffer[14], buffer[15]];
        let width = [buffer[16], buffer[17], buffer[18], buffer[19]];
        Ok((u32::from_le_bytes(width), u32::from_le_bytes(height)))
    }
}
