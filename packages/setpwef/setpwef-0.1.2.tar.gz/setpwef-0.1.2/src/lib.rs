use pyo3::prelude::*;

extern crate umya_spreadsheet;


#[pyfunction]
pub fn encrypt_excelfile(from_path: &str, to_path: &str, password: &str) {
    let _ = umya_spreadsheet::writer::xlsx::set_password(&from_path, &to_path, password);
}


#[pymodule]
fn setpwef(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(encrypt_excelfile, m)?)?;
    Ok(())
}