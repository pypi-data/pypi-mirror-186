/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Enum Utility Definitions                                                   *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

namespace mlir {
namespace sparse_tensor {
::llvm::StringRef stringifyStorageSpecifierKind(StorageSpecifierKind val) {
  switch (val) {
    case StorageSpecifierKind::DimSize: return "dim_sz";
    case StorageSpecifierKind::PtrMemSize: return "ptr_mem_sz";
    case StorageSpecifierKind::IdxMemSize: return "idx_mem_sz";
    case StorageSpecifierKind::ValMemSize: return "val_mem_sz";
  }
  return "";
}

::std::optional<StorageSpecifierKind> symbolizeStorageSpecifierKind(::llvm::StringRef str) {
  return ::llvm::StringSwitch<::std::optional<StorageSpecifierKind>>(str)
      .Case("dim_sz", StorageSpecifierKind::DimSize)
      .Case("ptr_mem_sz", StorageSpecifierKind::PtrMemSize)
      .Case("idx_mem_sz", StorageSpecifierKind::IdxMemSize)
      .Case("val_mem_sz", StorageSpecifierKind::ValMemSize)
      .Default(::std::nullopt);
}
::std::optional<StorageSpecifierKind> symbolizeStorageSpecifierKind(uint32_t value) {
  switch (value) {
  case 0: return StorageSpecifierKind::DimSize;
  case 1: return StorageSpecifierKind::PtrMemSize;
  case 2: return StorageSpecifierKind::IdxMemSize;
  case 3: return StorageSpecifierKind::ValMemSize;
  default: return ::std::nullopt;
  }
}

} // namespace sparse_tensor
} // namespace mlir

