/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Interface Declarations                                                     *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

namespace mlir {
namespace bufferization {
class BufferizableOpInterface;
namespace detail {
struct BufferizableOpInterfaceInterfaceTraits {
  struct Concept {
    bool (*bufferizesToAllocation)(const Concept *impl, ::mlir::Operation *, ::mlir::OpResult);
    bool (*bufferizesToMemoryRead)(const Concept *impl, ::mlir::Operation *, ::mlir::OpOperand &, const ::mlir::bufferization::AnalysisState &);
    bool (*bufferizesToMemoryWrite)(const Concept *impl, ::mlir::Operation *, ::mlir::OpOperand &, const ::mlir::bufferization::AnalysisState &);
    bool (*isMemoryWrite)(const Concept *impl, ::mlir::Operation *, ::mlir::OpResult, const ::mlir::bufferization::AnalysisState &);
    bool (*mustBufferizeInPlace)(const Concept *impl, ::mlir::Operation *, ::mlir::OpOperand &, const ::mlir::bufferization::AnalysisState &);
    ::mlir::SmallVector<::mlir::OpResult> (*getAliasingOpResult)(const Concept *impl, ::mlir::Operation *, ::mlir::OpOperand &, const ::mlir::bufferization::AnalysisState &);
    ::mlir::SmallVector<::mlir::OpOperand *> (*getAliasingOpOperand)(const Concept *impl, ::mlir::Operation *, ::mlir::OpResult, const ::mlir::bufferization::AnalysisState &);
    ::mlir::bufferization::BufferRelation (*bufferRelation)(const Concept *impl, ::mlir::Operation *, ::mlir::OpResult, const ::mlir::bufferization::AnalysisState &);
    ::mlir::LogicalResult (*resolveConflicts)(const Concept *impl, ::mlir::Operation *, ::mlir::RewriterBase &, const ::mlir::bufferization::AnalysisState &);
    ::mlir::LogicalResult (*bufferize)(const Concept *impl, ::mlir::Operation *, ::mlir::RewriterBase &, const ::mlir::bufferization::BufferizationOptions &);
    bool (*isWritable)(const Concept *impl, ::mlir::Operation *, ::mlir::Value, const ::mlir::bufferization::AnalysisState &);
    bool (*isNotConflicting)(const Concept *impl, ::mlir::Operation *, ::mlir::OpOperand *, ::mlir::OpOperand *, const ::mlir::bufferization::AnalysisState &);
    ::mlir::LogicalResult (*verifyAnalysis)(const Concept *impl, ::mlir::Operation *, const ::mlir::bufferization::AnalysisState &);
    ::mlir::FailureOr<::mlir::BaseMemRefType> (*getBufferType)(const Concept *impl, ::mlir::Operation *, ::mlir::Value, const ::mlir::bufferization::BufferizationOptions &, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType>);
    bool (*isRepetitiveRegion)(const Concept *impl, ::mlir::Operation *, unsigned);
  };
  template<typename ConcreteOp>
  class Model : public Concept {
  public:
    using Interface = ::mlir::bufferization::BufferizableOpInterface;
    Model() : Concept{bufferizesToAllocation, bufferizesToMemoryRead, bufferizesToMemoryWrite, isMemoryWrite, mustBufferizeInPlace, getAliasingOpResult, getAliasingOpOperand, bufferRelation, resolveConflicts, bufferize, isWritable, isNotConflicting, verifyAnalysis, getBufferType, isRepetitiveRegion} {}

    static inline bool bufferizesToAllocation(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult);
    static inline bool bufferizesToMemoryRead(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
    static inline bool bufferizesToMemoryWrite(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
    static inline bool isMemoryWrite(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
    static inline bool mustBufferizeInPlace(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::SmallVector<::mlir::OpResult> getAliasingOpResult(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::SmallVector<::mlir::OpOperand *> getAliasingOpOperand(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::bufferization::BufferRelation bufferRelation(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::LogicalResult resolveConflicts(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase & rewriter, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::LogicalResult bufferize(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase & rewriter, const ::mlir::bufferization::BufferizationOptions & options);
    static inline bool isWritable(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::AnalysisState & state);
    static inline bool isNotConflicting(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand * uRead, ::mlir::OpOperand * uWrite, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::LogicalResult verifyAnalysis(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::FailureOr<::mlir::BaseMemRefType> getBufferType(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::BufferizationOptions & options, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType> fixedTypes);
    static inline bool isRepetitiveRegion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, unsigned index);
  };
  template<typename ConcreteOp>
  class FallbackModel : public Concept {
  public:
    using Interface = ::mlir::bufferization::BufferizableOpInterface;
    FallbackModel() : Concept{bufferizesToAllocation, bufferizesToMemoryRead, bufferizesToMemoryWrite, isMemoryWrite, mustBufferizeInPlace, getAliasingOpResult, getAliasingOpOperand, bufferRelation, resolveConflicts, bufferize, isWritable, isNotConflicting, verifyAnalysis, getBufferType, isRepetitiveRegion} {}

    static inline bool bufferizesToAllocation(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult);
    static inline bool bufferizesToMemoryRead(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
    static inline bool bufferizesToMemoryWrite(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
    static inline bool isMemoryWrite(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
    static inline bool mustBufferizeInPlace(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::SmallVector<::mlir::OpResult> getAliasingOpResult(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::SmallVector<::mlir::OpOperand *> getAliasingOpOperand(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::bufferization::BufferRelation bufferRelation(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::LogicalResult resolveConflicts(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase & rewriter, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::LogicalResult bufferize(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase & rewriter, const ::mlir::bufferization::BufferizationOptions & options);
    static inline bool isWritable(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::AnalysisState & state);
    static inline bool isNotConflicting(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand * uRead, ::mlir::OpOperand * uWrite, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::LogicalResult verifyAnalysis(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, const ::mlir::bufferization::AnalysisState & state);
    static inline ::mlir::FailureOr<::mlir::BaseMemRefType> getBufferType(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::BufferizationOptions & options, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType> fixedTypes);
    static inline bool isRepetitiveRegion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, unsigned index);
  };
  template<typename ConcreteModel, typename ConcreteOp>
  class ExternalModel : public FallbackModel<ConcreteModel> {
  public:
    using ConcreteEntity = ConcreteOp;
    bool bufferizesToAllocation(::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult) const;
    bool bufferizesToMemoryRead(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand &opOperand, const ::mlir::bufferization::AnalysisState &state) const;
    bool bufferizesToMemoryWrite(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand &opOperand, const ::mlir::bufferization::AnalysisState &state) const;
    bool isMemoryWrite(::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState &state) const;
    bool mustBufferizeInPlace(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand &opOperand, const ::mlir::bufferization::AnalysisState &state) const;
    ::mlir::SmallVector<::mlir::OpResult> getAliasingOpResult(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand &opOperand, const ::mlir::bufferization::AnalysisState &state) const;
    ::mlir::SmallVector<::mlir::OpOperand *> getAliasingOpOperand(::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState &state) const;
    ::mlir::bufferization::BufferRelation bufferRelation(::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState &state) const;
    ::mlir::LogicalResult resolveConflicts(::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase &rewriter, const ::mlir::bufferization::AnalysisState &state) const;
    ::mlir::LogicalResult bufferize(::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase &rewriter, const ::mlir::bufferization::BufferizationOptions &options) const;
    bool isWritable(::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::AnalysisState &state) const;
    bool isNotConflicting(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand *uRead, ::mlir::OpOperand *uWrite, const ::mlir::bufferization::AnalysisState &state) const;
    ::mlir::LogicalResult verifyAnalysis(::mlir::Operation *tablegen_opaque_val, const ::mlir::bufferization::AnalysisState &state) const;
    ::mlir::FailureOr<::mlir::BaseMemRefType> getBufferType(::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::BufferizationOptions &options, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType> fixedTypes) const;
    bool isRepetitiveRegion(::mlir::Operation *tablegen_opaque_val, unsigned index) const;
  };
};template <typename ConcreteOp>
struct BufferizableOpInterfaceTrait;

} // namespace detail
class BufferizableOpInterface : public ::mlir::OpInterface<BufferizableOpInterface, detail::BufferizableOpInterfaceInterfaceTraits> {
public:
  using ::mlir::OpInterface<BufferizableOpInterface, detail::BufferizableOpInterfaceInterfaceTraits>::OpInterface;
  template <typename ConcreteOp>
  struct Trait : public detail::BufferizableOpInterfaceTrait<ConcreteOp> {};
  /// Return `true` if the given OpResult may bufferize to a new buffer
  /// allocation. If it is statically unknown if the given OpResult
  /// bufferizes to a buffer allocation, `true` should be returned.
  bool bufferizesToAllocation(::mlir::OpResult opResult);
  /// Return `true` if the given OpOperand bufferizes to a memory read. This
  /// method will never be called on OpOperands that do not have a tensor
  /// type.
  /// 
  /// Note: It is always safe to consider an OpOperand as a memory read,
  /// even if it does actually not read; however, this can introduce
  /// unnecessary out-of-place bufferization decisions. One-Shot Analysis
  /// considers OpOperands of unknown ops (that do not implement this
  /// interface) as reading OpOperands.
  bool bufferizesToMemoryRead(::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
  /// Return `true` if the given OpOperand bufferizes to a memory write.
  /// 
  /// This method will never be called on OpOperands that do not have a
  /// tensor type.
  /// 
  /// This method will never be called on OpOperands that do not have an
  /// aliasing OpResult. Intuitively, it does not make sense for an
  /// OpOperand to bufferize to a memory write without returning an aliasing
  /// tensor, because the write would have no visible effect outside of the
  /// op.
  /// 
  /// Note: It is always safe to consider an OpOperand as a memory write,
  /// even if it does actually not write; however, this can introduce
  /// unnecessary out-of-place bufferization decisions. One-Shot Analysis
  /// considers OpOperands of unknown ops (that do not implement this
  /// interface) as writing OpOperands.
  bool bufferizesToMemoryWrite(::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
  /// Return `true` if the given OpResult is a memory write. This is the
  /// case if in the following cases:
  /// 
  /// * The corresponding aliasing OpOperand bufferizes to a memory write.
  /// * Or: There is no corresponding aliasing OpOperand.
  /// 
  /// If the OpResult has multiple aliasing OpOperands, this method
  /// returns `true` if at least one of them bufferizes to a memory write.
  bool isMemoryWrite(::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
  /// Return `true` if the given OpOperand must bufferize in-place. Alias
  /// sets and inplace attributes will be set up accordingly before making
  /// any other bufferization decisions. This method will never be called on
  /// OpOperands that do not have a tensor type.
  bool mustBufferizeInPlace(::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
  /// Return the OpResult that aliases with a given OpOperand when
  /// bufferized in-place. This method will never be called on OpOperands
  /// that do not have a tensor type.
  /// 
  /// Note: This method can return multiple OpResults, indicating that a
  /// given OpOperand may at runtime alias with any (or multiple) of the
  /// returned OpResults.
  ::mlir::SmallVector<::mlir::OpResult> getAliasingOpResult(::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state);
  /// Return the OpOperands that alias with a given OpResult when
  /// bufferized in-place. This method will never be called on OpResults
  /// that do not have a tensor type.
  /// 
  /// By default, this method is the inverse of `getAliasingOpResult`. Ops
  /// with a region that yield values may want to override this method to
  /// return the OpOperands that are yielded by the terminator.
  /// 
  /// Note: This method can return multiple OpOperands, indicating that the
  /// given OpResult may at runtime alias with any (or multiple) of the
  /// returned OpOperands. This can be useful for branches and for ops such
  /// as `arith.select`.
  ::mlir::SmallVector<::mlir::OpOperand *> getAliasingOpOperand(::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
  /// Return the buffer relation between the given OpResult and its aliasing
  /// OpOperands when bufferized in-place. Most OpOperands have an
  /// "equivalence" relation. This method will never be called on OpResults
  /// that do not have a tensor type. It will also never be called on
  /// OpResults that do not have at least one aliasing OpOperand.
  /// 
  /// TODO: Support other relations such as "OpOperand is included in
  /// OpResult".
  ::mlir::bufferization::BufferRelation bufferRelation(::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state);
  /// Resolve all inplacability conflicts by inserting explicit
  /// `bufferization.alloc_tensor` ops. Examples of inplacability conflicts
  /// are read-after-write conflicts or writes into non-writable buffers.
  /// 
  /// This method should rewrite the IR in such a way that for each tensor
  /// OpOperand t, buffer(t) can be directly used when during bufferization.
  /// The bufferization does no longer have to care about inplacability
  /// conflicts.
  /// 
  /// This method can query analysis information from the given analysis
  /// state.
  ::mlir::LogicalResult resolveConflicts(::mlir::RewriterBase & rewriter, const ::mlir::bufferization::AnalysisState & state);
  /// Bufferize this op, i.e., rewrite it into a memref-based equivalent.
  /// Buffers of tensor SSA values can be retrieved via `getBuffer`.
  /// Uses of tensor results of the existing tensor op can be replaced with
  /// `replaceOpWithBufferizedValues` or `replaceOpWithNewBufferizedOp`.
  /// These two functions automatically handle the tensor-to-memref type
  /// conversion.
  /// 
  /// The implementation of this method must be consistent with the
  /// remaining methods, in particular `getAliasingOpOperand`. I.e., a
  /// tensor result `r` may only be replaced with:
  /// a) A buffer that aliases one of buffers in getAliasingOpOperand(r).
  /// b) Or: A newly allocated buffer.
  /// 
  /// This method will never be called on ops that do not have at least one
  /// tensor operand/result.
  /// 
  /// The return value of this method indicates whether there was an error
  /// while bufferizing this op (such as failing to create a new buffer
  /// allocation op). The bufferization driver immediately stops bufferizing
  /// the input IR and returns `failure` in that case. If this op is
  /// expected to survive bufferization, `success` should be returned
  /// (together with `allow-unknown-ops` enabled).
  ::mlir::LogicalResult bufferize(::mlir::RewriterBase & rewriter, const ::mlir::bufferization::BufferizationOptions & options);
  /// Return `true` if the given Value can be written to in-place. Value is
  /// either an OpResult of this operation or a BlockArgument of a block of
  /// this operation.
  /// 
  /// Most OpResult buffers can be written to, but some ops such as
  /// ConstantOp may bufferize to non-writable (read-only) memory locations.
  /// Therefore, by default, this method returns `true` for OpResults. This
  /// method will never be called on OpResults that do not have a tensor
  /// type.
  /// 
  /// Whether a BlockArgument can be written to or not depends on the
  /// operation. This method conservatively returns `false`. This method
  /// will never be called on BlockArguments that do not have a tensor type.
  bool isWritable(::mlir::Value value, const ::mlir::bufferization::AnalysisState & state);
  /// Return `true` if the `uRead` and `uWrite` do not constitute a RaW
  /// conflict. If they are conflicting or if it is unknown whether they are
  /// conflicting, return `false`. This method will never be called with
  /// OpOperands that do not have a tensor type. At least one of the two
  /// given OpOperands belongs to this operation.
  /// 
  /// This method can be implemented to specify custom RaW analysis rules.
  /// If this method returns `true` the given OpOperands are not considered
  /// to be conflicting and do not force out-of-place bufferization. (There
  /// may still be other conflicts that do.)
  bool isNotConflicting(::mlir::OpOperand * uRead, ::mlir::OpOperand * uWrite, const ::mlir::bufferization::AnalysisState & state);
  /// Return `failure` if this op does not pass the analysis. This method
  /// is run during One-Shot Bufferize (after all post-analysis steps). If
  /// the op does not pass the analysis, bufferization is aborted.
  /// 
  /// This method can be used to check expected invariants and limitations
  /// of the current bufferization implementation.
  ::mlir::LogicalResult verifyAnalysis(const ::mlir::bufferization::AnalysisState & state);
  /// Return the bufferized type of the given tensor value (without
  /// bufferizing the IR). The value is either a BlockArgument of a block
  /// that belongs to this op or an OpResult of the given op.
  /// 
  /// This method is useful when the bufferized type of value must be
  /// predicted before modifying any IR.
  ::mlir::FailureOr<::mlir::BaseMemRefType> getBufferType(::mlir::Value value, const ::mlir::bufferization::BufferizationOptions & options, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType> fixedTypes);
  /// Return `true` if the given region of this op is repetitive. By default
  /// this information is queried from the `RegionBranchOpInterface`. Ops
  /// that do not implement this inferface can override this method to
  /// declare regions as repetitive.
  /// 
  /// The RaW conflict detection of One-Shot Analysis is more strict inside
  /// repetitive regions: Op dominance cannot always be used to rule out
  /// certain potential conflicts (e.g., a conflicting write happening after
  /// a read), because there may not be a meaningful ordering of certain ops
  /// that are executed multiple times. This is described in more detail in
  /// documentation of One-Shot Analysis.
  bool isRepetitiveRegion(unsigned index);

    /// Resolve out-of-place tensor OpOperands with explicit allocations in the
    /// form of `bufferization.alloc_tensor` ops.
    LogicalResult resolveTensorOpOperandConflicts(
        RewriterBase &rewriter, const AnalysisState &state);

    /// Return `true` if the given OpOperand creates an alias but does neither
    /// read nor write. This implies that `bufferizesToMemoryRead` and
    /// `bufferizesToMemoryWrite` must return `false`. This method will never
    /// be called on OpOperands that do not have a tensor type.
    ///
    /// Examples of such ops are `tensor.extract_slice` and `tensor.cast`.
    bool bufferizesToAliasOnly(OpOperand &opOperand,
                               const AnalysisState &state) {
      auto bufferizableOp =
          cast<BufferizableOpInterface>(getOperation());
      return !bufferizableOp.bufferizesToMemoryRead(opOperand, state)
          && !bufferizableOp.bufferizesToMemoryWrite(opOperand, state)
          && !bufferizableOp.getAliasingOpResult(opOperand, state).empty();
    }
  
};
namespace detail {
  template <typename ConcreteOp>
  struct BufferizableOpInterfaceTrait : public ::mlir::OpInterface<BufferizableOpInterface, detail::BufferizableOpInterfaceInterfaceTraits>::Trait<ConcreteOp> {
    /// Return `true` if the given OpResult may bufferize to a new buffer
    /// allocation. If it is statically unknown if the given OpResult
    /// bufferizes to a buffer allocation, `true` should be returned.
    bool bufferizesToAllocation(::mlir::OpResult opResult) {
      return false;
    }
    /// Return `true` if the given OpOperand bufferizes to a memory read. This
    /// method will never be called on OpOperands that do not have a tensor
    /// type.
    /// 
    /// Note: It is always safe to consider an OpOperand as a memory read,
    /// even if it does actually not read; however, this can introduce
    /// unnecessary out-of-place bufferization decisions. One-Shot Analysis
    /// considers OpOperands of unknown ops (that do not implement this
    /// interface) as reading OpOperands.
    bool bufferizesToMemoryRead(::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
      // Does not have to be implemented for ops without tensor OpOperands.
          llvm_unreachable("bufferizesToMemoryRead not implemented");
    }
    /// Return `true` if the given OpOperand bufferizes to a memory write.
    /// 
    /// This method will never be called on OpOperands that do not have a
    /// tensor type.
    /// 
    /// This method will never be called on OpOperands that do not have an
    /// aliasing OpResult. Intuitively, it does not make sense for an
    /// OpOperand to bufferize to a memory write without returning an aliasing
    /// tensor, because the write would have no visible effect outside of the
    /// op.
    /// 
    /// Note: It is always safe to consider an OpOperand as a memory write,
    /// even if it does actually not write; however, this can introduce
    /// unnecessary out-of-place bufferization decisions. One-Shot Analysis
    /// considers OpOperands of unknown ops (that do not implement this
    /// interface) as writing OpOperands.
    bool bufferizesToMemoryWrite(::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
      // Does not have to be implemented for ops without tensor OpOperands.
          // Does not have to be implemented for OpOperands that do not have an
          // aliasing OpResult.
          llvm_unreachable("bufferizesToMemoryWrite not implemented");
    }
    /// Return `true` if the given OpResult is a memory write. This is the
    /// case if in the following cases:
    /// 
    /// * The corresponding aliasing OpOperand bufferizes to a memory write.
    /// * Or: There is no corresponding aliasing OpOperand.
    /// 
    /// If the OpResult has multiple aliasing OpOperands, this method
    /// returns `true` if at least one of them bufferizes to a memory write.
    bool isMemoryWrite(::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
      auto bufferizableOp =
                cast<BufferizableOpInterface>((*static_cast<ConcreteOp *>(this)).getOperation());
            SmallVector<OpOperand*> opOperands =
              bufferizableOp.getAliasingOpOperand(opResult, state);
            if (opOperands.empty())
              return true;
            return llvm::any_of(
                opOperands,
                [&](OpOperand *operand) {
                  return bufferizableOp.bufferizesToMemoryWrite(*operand,
                                                                state);
                });
    }
    /// Return `true` if the given OpOperand must bufferize in-place. Alias
    /// sets and inplace attributes will be set up accordingly before making
    /// any other bufferization decisions. This method will never be called on
    /// OpOperands that do not have a tensor type.
    bool mustBufferizeInPlace(::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
      return false;
    }
    /// Return the OpResult that aliases with a given OpOperand when
    /// bufferized in-place. This method will never be called on OpOperands
    /// that do not have a tensor type.
    /// 
    /// Note: This method can return multiple OpResults, indicating that a
    /// given OpOperand may at runtime alias with any (or multiple) of the
    /// returned OpResults.
    ::mlir::SmallVector<::mlir::OpResult> getAliasingOpResult(::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
      // Does not have to be implemented for ops without tensor OpOperands.
          llvm_unreachable("getAliasingOpResult not implemented");
    }
    /// Return the OpOperands that alias with a given OpResult when
    /// bufferized in-place. This method will never be called on OpResults
    /// that do not have a tensor type.
    /// 
    /// By default, this method is the inverse of `getAliasingOpResult`. Ops
    /// with a region that yield values may want to override this method to
    /// return the OpOperands that are yielded by the terminator.
    /// 
    /// Note: This method can return multiple OpOperands, indicating that the
    /// given OpResult may at runtime alias with any (or multiple) of the
    /// returned OpOperands. This can be useful for branches and for ops such
    /// as `arith.select`.
    ::mlir::SmallVector<::mlir::OpOperand *> getAliasingOpOperand(::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
      assert(opResult.getType().isa<TensorType>() &&
                 "expected OpResult with tensor type");
          SmallVector<OpOperand *> result;
          auto bufferizableOp =
              cast<BufferizableOpInterface>((*static_cast<ConcreteOp *>(this)).getOperation());
          for (OpOperand &opOperand : (*static_cast<ConcreteOp *>(this)).getOperation()->getOpOperands()) {
            if (!opOperand.get().getType().isa<TensorType>())
              continue;
            SmallVector<OpResult> aliasingOpResults =
                bufferizableOp.getAliasingOpResult(opOperand, state);
            if (llvm::is_contained(aliasingOpResults, opResult))
              result.push_back(&opOperand);
          }
          return result;
    }
    /// Return the buffer relation between the given OpResult and its aliasing
    /// OpOperands when bufferized in-place. Most OpOperands have an
    /// "equivalence" relation. This method will never be called on OpResults
    /// that do not have a tensor type. It will also never be called on
    /// OpResults that do not have at least one aliasing OpOperand.
    /// 
    /// TODO: Support other relations such as "OpOperand is included in
    /// OpResult".
    ::mlir::bufferization::BufferRelation bufferRelation(::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
      // Does not have to be implemented for ops without tensor OpResults
          // that have an aliasing OpOperand.
          llvm_unreachable("bufferRelation not implemented");
    }
    /// Resolve all inplacability conflicts by inserting explicit
    /// `bufferization.alloc_tensor` ops. Examples of inplacability conflicts
    /// are read-after-write conflicts or writes into non-writable buffers.
    /// 
    /// This method should rewrite the IR in such a way that for each tensor
    /// OpOperand t, buffer(t) can be directly used when during bufferization.
    /// The bufferization does no longer have to care about inplacability
    /// conflicts.
    /// 
    /// This method can query analysis information from the given analysis
    /// state.
    ::mlir::LogicalResult resolveConflicts(::mlir::RewriterBase & rewriter, const ::mlir::bufferization::AnalysisState & state) {
      auto bufferizableOp =
              cast<BufferizableOpInterface>((*static_cast<ConcreteOp *>(this)).getOperation());
          return bufferizableOp.resolveTensorOpOperandConflicts(
              rewriter, state);
    }
    /// Bufferize this op, i.e., rewrite it into a memref-based equivalent.
    /// Buffers of tensor SSA values can be retrieved via `getBuffer`.
    /// Uses of tensor results of the existing tensor op can be replaced with
    /// `replaceOpWithBufferizedValues` or `replaceOpWithNewBufferizedOp`.
    /// These two functions automatically handle the tensor-to-memref type
    /// conversion.
    /// 
    /// The implementation of this method must be consistent with the
    /// remaining methods, in particular `getAliasingOpOperand`. I.e., a
    /// tensor result `r` may only be replaced with:
    /// a) A buffer that aliases one of buffers in getAliasingOpOperand(r).
    /// b) Or: A newly allocated buffer.
    /// 
    /// This method will never be called on ops that do not have at least one
    /// tensor operand/result.
    /// 
    /// The return value of this method indicates whether there was an error
    /// while bufferizing this op (such as failing to create a new buffer
    /// allocation op). The bufferization driver immediately stops bufferizing
    /// the input IR and returns `failure` in that case. If this op is
    /// expected to survive bufferization, `success` should be returned
    /// (together with `allow-unknown-ops` enabled).
    ::mlir::LogicalResult bufferize(::mlir::RewriterBase & rewriter, const ::mlir::bufferization::BufferizationOptions & options) {
      llvm_unreachable("bufferize not implemented");
          return failure();
    }
    /// Return `true` if the given Value can be written to in-place. Value is
    /// either an OpResult of this operation or a BlockArgument of a block of
    /// this operation.
    /// 
    /// Most OpResult buffers can be written to, but some ops such as
    /// ConstantOp may bufferize to non-writable (read-only) memory locations.
    /// Therefore, by default, this method returns `true` for OpResults. This
    /// method will never be called on OpResults that do not have a tensor
    /// type.
    /// 
    /// Whether a BlockArgument can be written to or not depends on the
    /// operation. This method conservatively returns `false`. This method
    /// will never be called on BlockArguments that do not have a tensor type.
    bool isWritable(::mlir::Value value, const ::mlir::bufferization::AnalysisState & state) {
      return value.isa<OpResult>();
    }
    /// Return `true` if the `uRead` and `uWrite` do not constitute a RaW
    /// conflict. If they are conflicting or if it is unknown whether they are
    /// conflicting, return `false`. This method will never be called with
    /// OpOperands that do not have a tensor type. At least one of the two
    /// given OpOperands belongs to this operation.
    /// 
    /// This method can be implemented to specify custom RaW analysis rules.
    /// If this method returns `true` the given OpOperands are not considered
    /// to be conflicting and do not force out-of-place bufferization. (There
    /// may still be other conflicts that do.)
    bool isNotConflicting(::mlir::OpOperand * uRead, ::mlir::OpOperand * uWrite, const ::mlir::bufferization::AnalysisState & state) {
      return false;
    }
    /// Return `failure` if this op does not pass the analysis. This method
    /// is run during One-Shot Bufferize (after all post-analysis steps). If
    /// the op does not pass the analysis, bufferization is aborted.
    /// 
    /// This method can be used to check expected invariants and limitations
    /// of the current bufferization implementation.
    ::mlir::LogicalResult verifyAnalysis(const ::mlir::bufferization::AnalysisState & state) {
      return success();
    }
    /// Return the bufferized type of the given tensor value (without
    /// bufferizing the IR). The value is either a BlockArgument of a block
    /// that belongs to this op or an OpResult of the given op.
    /// 
    /// This method is useful when the bufferized type of value must be
    /// predicted before modifying any IR.
    ::mlir::FailureOr<::mlir::BaseMemRefType> getBufferType(::mlir::Value value, const ::mlir::bufferization::BufferizationOptions & options, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType> fixedTypes) {
      assert(getOwnerOfValue(value) == (*static_cast<ConcreteOp *>(this)).getOperation() &&
                 "expected that value belongs to this op");
          return bufferization::detail::defaultGetBufferType(
              value, options, fixedTypes);
    }
    /// Return `true` if the given region of this op is repetitive. By default
    /// this information is queried from the `RegionBranchOpInterface`. Ops
    /// that do not implement this inferface can override this method to
    /// declare regions as repetitive.
    /// 
    /// The RaW conflict detection of One-Shot Analysis is more strict inside
    /// repetitive regions: Op dominance cannot always be used to rule out
    /// certain potential conflicts (e.g., a conflicting write happening after
    /// a read), because there may not be a meaningful ordering of certain ops
    /// that are executed multiple times. This is described in more detail in
    /// documentation of One-Shot Analysis.
    bool isRepetitiveRegion(unsigned index) {
      return mlir::bufferization::detail::defaultIsRepetitiveRegion(
              cast<BufferizableOpInterface>((*static_cast<ConcreteOp *>(this)).getOperation()), index);
    }
  };
}// namespace detail
} // namespace bufferization
} // namespace mlir
namespace mlir {
namespace bufferization {
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::bufferizesToAllocation(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).bufferizesToAllocation(opResult);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::bufferizesToMemoryRead(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).bufferizesToMemoryRead(opOperand, state);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::bufferizesToMemoryWrite(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).bufferizesToMemoryWrite(opOperand, state);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::isMemoryWrite(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).isMemoryWrite(opResult, state);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::mustBufferizeInPlace(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).mustBufferizeInPlace(opOperand, state);
}
template<typename ConcreteOp>
::mlir::SmallVector<::mlir::OpResult> detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::getAliasingOpResult(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).getAliasingOpResult(opOperand, state);
}
template<typename ConcreteOp>
::mlir::SmallVector<::mlir::OpOperand *> detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::getAliasingOpOperand(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).getAliasingOpOperand(opResult, state);
}
template<typename ConcreteOp>
::mlir::bufferization::BufferRelation detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::bufferRelation(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).bufferRelation(opResult, state);
}
template<typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::resolveConflicts(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase & rewriter, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).resolveConflicts(rewriter, state);
}
template<typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::bufferize(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase & rewriter, const ::mlir::bufferization::BufferizationOptions & options) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).bufferize(rewriter, options);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::isWritable(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).isWritable(value, state);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::isNotConflicting(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand * uRead, ::mlir::OpOperand * uWrite, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).isNotConflicting(uRead, uWrite, state);
}
template<typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::verifyAnalysis(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, const ::mlir::bufferization::AnalysisState & state) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).verifyAnalysis(state);
}
template<typename ConcreteOp>
::mlir::FailureOr<::mlir::BaseMemRefType> detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::getBufferType(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::BufferizationOptions & options, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType> fixedTypes) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).getBufferType(value, options, fixedTypes);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::Model<ConcreteOp>::isRepetitiveRegion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, unsigned index) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).isRepetitiveRegion(index);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::bufferizesToAllocation(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult) {
  return static_cast<const ConcreteOp *>(impl)->bufferizesToAllocation(tablegen_opaque_val, opResult);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::bufferizesToMemoryRead(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->bufferizesToMemoryRead(tablegen_opaque_val, opOperand, state);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::bufferizesToMemoryWrite(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->bufferizesToMemoryWrite(tablegen_opaque_val, opOperand, state);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::isMemoryWrite(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->isMemoryWrite(tablegen_opaque_val, opResult, state);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::mustBufferizeInPlace(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->mustBufferizeInPlace(tablegen_opaque_val, opOperand, state);
}
template<typename ConcreteOp>
::mlir::SmallVector<::mlir::OpResult> detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::getAliasingOpResult(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand & opOperand, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->getAliasingOpResult(tablegen_opaque_val, opOperand, state);
}
template<typename ConcreteOp>
::mlir::SmallVector<::mlir::OpOperand *> detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::getAliasingOpOperand(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->getAliasingOpOperand(tablegen_opaque_val, opResult, state);
}
template<typename ConcreteOp>
::mlir::bufferization::BufferRelation detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::bufferRelation(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->bufferRelation(tablegen_opaque_val, opResult, state);
}
template<typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::resolveConflicts(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase & rewriter, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->resolveConflicts(tablegen_opaque_val, rewriter, state);
}
template<typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::bufferize(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase & rewriter, const ::mlir::bufferization::BufferizationOptions & options) {
  return static_cast<const ConcreteOp *>(impl)->bufferize(tablegen_opaque_val, rewriter, options);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::isWritable(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->isWritable(tablegen_opaque_val, value, state);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::isNotConflicting(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand * uRead, ::mlir::OpOperand * uWrite, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->isNotConflicting(tablegen_opaque_val, uRead, uWrite, state);
}
template<typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::verifyAnalysis(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, const ::mlir::bufferization::AnalysisState & state) {
  return static_cast<const ConcreteOp *>(impl)->verifyAnalysis(tablegen_opaque_val, state);
}
template<typename ConcreteOp>
::mlir::FailureOr<::mlir::BaseMemRefType> detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::getBufferType(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::BufferizationOptions & options, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType> fixedTypes) {
  return static_cast<const ConcreteOp *>(impl)->getBufferType(tablegen_opaque_val, value, options, fixedTypes);
}
template<typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::isRepetitiveRegion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val, unsigned index) {
  return static_cast<const ConcreteOp *>(impl)->isRepetitiveRegion(tablegen_opaque_val, index);
}
template<typename ConcreteModel, typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::bufferizesToAllocation(::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult) const {
return false;
}
template<typename ConcreteModel, typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::bufferizesToMemoryRead(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand &opOperand, const ::mlir::bufferization::AnalysisState &state) const {
// Does not have to be implemented for ops without tensor OpOperands.
          llvm_unreachable("bufferizesToMemoryRead not implemented");
}
template<typename ConcreteModel, typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::bufferizesToMemoryWrite(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand &opOperand, const ::mlir::bufferization::AnalysisState &state) const {
// Does not have to be implemented for ops without tensor OpOperands.
          // Does not have to be implemented for OpOperands that do not have an
          // aliasing OpResult.
          llvm_unreachable("bufferizesToMemoryWrite not implemented");
}
template<typename ConcreteModel, typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::isMemoryWrite(::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState &state) const {
auto bufferizableOp =
                cast<BufferizableOpInterface>((llvm::cast<ConcreteOp>(tablegen_opaque_val)).getOperation());
            SmallVector<OpOperand*> opOperands =
              bufferizableOp.getAliasingOpOperand(opResult, state);
            if (opOperands.empty())
              return true;
            return llvm::any_of(
                opOperands,
                [&](OpOperand *operand) {
                  return bufferizableOp.bufferizesToMemoryWrite(*operand,
                                                                state);
                });
}
template<typename ConcreteModel, typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::mustBufferizeInPlace(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand &opOperand, const ::mlir::bufferization::AnalysisState &state) const {
return false;
}
template<typename ConcreteModel, typename ConcreteOp>
::mlir::SmallVector<::mlir::OpResult> detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::getAliasingOpResult(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand &opOperand, const ::mlir::bufferization::AnalysisState &state) const {
// Does not have to be implemented for ops without tensor OpOperands.
          llvm_unreachable("getAliasingOpResult not implemented");
}
template<typename ConcreteModel, typename ConcreteOp>
::mlir::SmallVector<::mlir::OpOperand *> detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::getAliasingOpOperand(::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState &state) const {
assert(opResult.getType().isa<TensorType>() &&
                 "expected OpResult with tensor type");
          SmallVector<OpOperand *> result;
          auto bufferizableOp =
              cast<BufferizableOpInterface>((llvm::cast<ConcreteOp>(tablegen_opaque_val)).getOperation());
          for (OpOperand &opOperand : (llvm::cast<ConcreteOp>(tablegen_opaque_val)).getOperation()->getOpOperands()) {
            if (!opOperand.get().getType().isa<TensorType>())
              continue;
            SmallVector<OpResult> aliasingOpResults =
                bufferizableOp.getAliasingOpResult(opOperand, state);
            if (llvm::is_contained(aliasingOpResults, opResult))
              result.push_back(&opOperand);
          }
          return result;
}
template<typename ConcreteModel, typename ConcreteOp>
::mlir::bufferization::BufferRelation detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::bufferRelation(::mlir::Operation *tablegen_opaque_val, ::mlir::OpResult opResult, const ::mlir::bufferization::AnalysisState &state) const {
// Does not have to be implemented for ops without tensor OpResults
          // that have an aliasing OpOperand.
          llvm_unreachable("bufferRelation not implemented");
}
template<typename ConcreteModel, typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::resolveConflicts(::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase &rewriter, const ::mlir::bufferization::AnalysisState &state) const {
auto bufferizableOp =
              cast<BufferizableOpInterface>((llvm::cast<ConcreteOp>(tablegen_opaque_val)).getOperation());
          return bufferizableOp.resolveTensorOpOperandConflicts(
              rewriter, state);
}
template<typename ConcreteModel, typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::bufferize(::mlir::Operation *tablegen_opaque_val, ::mlir::RewriterBase &rewriter, const ::mlir::bufferization::BufferizationOptions &options) const {
llvm_unreachable("bufferize not implemented");
          return failure();
}
template<typename ConcreteModel, typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::isWritable(::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::AnalysisState &state) const {
return value.isa<OpResult>();
}
template<typename ConcreteModel, typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::isNotConflicting(::mlir::Operation *tablegen_opaque_val, ::mlir::OpOperand *uRead, ::mlir::OpOperand *uWrite, const ::mlir::bufferization::AnalysisState &state) const {
return false;
}
template<typename ConcreteModel, typename ConcreteOp>
::mlir::LogicalResult detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::verifyAnalysis(::mlir::Operation *tablegen_opaque_val, const ::mlir::bufferization::AnalysisState &state) const {
return success();
}
template<typename ConcreteModel, typename ConcreteOp>
::mlir::FailureOr<::mlir::BaseMemRefType> detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::getBufferType(::mlir::Operation *tablegen_opaque_val, ::mlir::Value value, const ::mlir::bufferization::BufferizationOptions &options, const ::mlir::DenseMap<::mlir::Value, ::mlir::BaseMemRefType> fixedTypes) const {
assert(getOwnerOfValue(value) == (llvm::cast<ConcreteOp>(tablegen_opaque_val)).getOperation() &&
                 "expected that value belongs to this op");
          return bufferization::detail::defaultGetBufferType(
              value, options, fixedTypes);
}
template<typename ConcreteModel, typename ConcreteOp>
bool detail::BufferizableOpInterfaceInterfaceTraits::ExternalModel<ConcreteModel, ConcreteOp>::isRepetitiveRegion(::mlir::Operation *tablegen_opaque_val, unsigned index) const {
return mlir::bufferization::detail::defaultIsRepetitiveRegion(
              cast<BufferizableOpInterface>((llvm::cast<ConcreteOp>(tablegen_opaque_val)).getOperation()), index);
}
} // namespace bufferization
} // namespace mlir
