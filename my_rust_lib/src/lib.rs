#[no_mangle]
pub extern "C" fn dll_add(a: i32, b: i32) -> i32 {
    a + b
}
