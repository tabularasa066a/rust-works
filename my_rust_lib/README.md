# Rustでdllを作りPythonから呼び出す

## 手順
### [1] Rustでのdllプロジェクト作成
```bash
cargo new my_rust_lib --lib
```

### [2] `Cargo.toml`の編集
```toml
[package]
name = "my_rust_lib"
version = "0.1.0"
edition = "2021"

[dependencies]

[lib]
crate-type = ["cdylib"] # C仕様の動的ライブラリに変換する旨
```

### [3] `src/lib.rs`にdll関数を実装
```rust
#[no_mangle]
pub extern "C" fn dll_add(a: i32, b: i32) -> i32 {
    a + b
}
```

### [4] プロジェクトをビルド
```bash
cd my_rust_lib
cargo build --release
# my_rust_lib/target/release内にmy_rust_lib.dllができる
# これをコピーしてPythonプロジェクトの配下に配置
```

### [5] Pythonからの呼出し
以下の内容を`call.py`として保存
```python
from ctypes import cdll, c_int

lib = cdll.LoadLibrary("./my_rust_lib.dll")
print(lib.dll_add(10, 23))
```

### [6] `call.py`の実行
```bash
python3 call.py # 33と出力
```

## 参考
- [Rustで.libや.dllを作り、C++から呼び出す](https://suzulang.com/call-rust-lib-from-cpp/)
- [要点がまとまってる](https://qiita.com/wada314/items/8e31ee8c5720d31f5875)
