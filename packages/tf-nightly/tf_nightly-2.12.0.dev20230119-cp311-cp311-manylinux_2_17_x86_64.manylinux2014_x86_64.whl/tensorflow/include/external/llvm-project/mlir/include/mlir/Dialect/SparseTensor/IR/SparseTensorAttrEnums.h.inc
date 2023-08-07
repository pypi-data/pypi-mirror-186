/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Enum Utility Declarations                                                  *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

namespace mlir {
namespace sparse_tensor {
// sparse tensor storage specifier kind
enum class StorageSpecifierKind : uint32_t {
  DimSize = 0,
  PtrMemSize = 1,
  IdxMemSize = 2,
  ValMemSize = 3,
};

::std::optional<StorageSpecifierKind> symbolizeStorageSpecifierKind(uint32_t);
::llvm::StringRef stringifyStorageSpecifierKind(StorageSpecifierKind);
::std::optional<StorageSpecifierKind> symbolizeStorageSpecifierKind(::llvm::StringRef);
inline constexpr unsigned getMaxEnumValForStorageSpecifierKind() {
  return 3;
}


inline ::llvm::StringRef stringifyEnum(StorageSpecifierKind enumValue) {
  return stringifyStorageSpecifierKind(enumValue);
}

template <typename EnumType>
::std::optional<EnumType> symbolizeEnum(::llvm::StringRef);

template <>
inline ::std::optional<StorageSpecifierKind> symbolizeEnum<StorageSpecifierKind>(::llvm::StringRef str) {
  return symbolizeStorageSpecifierKind(str);
}
} // namespace sparse_tensor
} // namespace mlir

namespace mlir {
template <typename T, typename>
struct FieldParser;

template<>
struct FieldParser<::mlir::sparse_tensor::StorageSpecifierKind, ::mlir::sparse_tensor::StorageSpecifierKind> {
  template <typename ParserT>
  static FailureOr<::mlir::sparse_tensor::StorageSpecifierKind> parse(ParserT &parser) {
    // Parse the keyword/string containing the enum.
    std::string enumKeyword;
    auto loc = parser.getCurrentLocation();
    if (failed(parser.parseOptionalKeywordOrString(&enumKeyword)))
      return parser.emitError(loc, "expected keyword for sparse tensor storage specifier kind");

    // Symbolize the keyword.
    if (::std::optional<::mlir::sparse_tensor::StorageSpecifierKind> attr = ::mlir::sparse_tensor::symbolizeEnum<::mlir::sparse_tensor::StorageSpecifierKind>(enumKeyword))
      return *attr;
    return parser.emitError(loc, "invalid sparse tensor storage specifier kind specification: ") << enumKeyword;
  }
};
} // namespace mlir

namespace llvm {
inline ::llvm::raw_ostream &operator<<(::llvm::raw_ostream &p, ::mlir::sparse_tensor::StorageSpecifierKind value) {
  auto valueStr = stringifyEnum(value);
  return p << valueStr;
}
} // namespace llvm

namespace llvm {
template<> struct DenseMapInfo<::mlir::sparse_tensor::StorageSpecifierKind> {
  using StorageInfo = ::llvm::DenseMapInfo<uint32_t>;

  static inline ::mlir::sparse_tensor::StorageSpecifierKind getEmptyKey() {
    return static_cast<::mlir::sparse_tensor::StorageSpecifierKind>(StorageInfo::getEmptyKey());
  }

  static inline ::mlir::sparse_tensor::StorageSpecifierKind getTombstoneKey() {
    return static_cast<::mlir::sparse_tensor::StorageSpecifierKind>(StorageInfo::getTombstoneKey());
  }

  static unsigned getHashValue(const ::mlir::sparse_tensor::StorageSpecifierKind &val) {
    return StorageInfo::getHashValue(static_cast<uint32_t>(val));
  }

  static bool isEqual(const ::mlir::sparse_tensor::StorageSpecifierKind &lhs, const ::mlir::sparse_tensor::StorageSpecifierKind &rhs) {
    return lhs == rhs;
  }
};
}

