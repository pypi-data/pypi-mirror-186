# Copyright 2018 by Au-Zone Technologies.  All Rights Reserved.
#
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential.
#
# This source code is provided solely for runtime interpretation by Python.
# Modifying or copying any source code is explicitly forbidden.

from cffi import FFI
from os import environ
from os.path import isdir, join

# The following is taken from deepview-rt.h with the various preprocessor
# defintions removed.  It needs to be maintained along with the deepview-rt.h.
#
# cat include/deepview_ops.h \
#   | cpp -DDEEPVIEW_RT_NO_INCLUDES -D__STDC_NO_VLA__ -Iinclude - \
#   | grep -v -e "^#" \
#   | grep -v extern \
#   | grep -v NN_AVAILABLE_SINCE \
#   | grep -v NN_API \
#   | grep -v "__attribute__" \
#   | grep -v -e '^$' > librt.h
#
ffi = FFI()
ffi.cdef('''
typedef enum {
    NN_SUCCESS = 0,
    NN_ERROR_INTERNAL,
    NN_ERROR_INVALID_HANDLE,
    NN_ERROR_OUT_OF_MEMORY,
    NN_ERROR_OUT_OF_RESOURCES,
    NN_ERROR_NOT_IMPLEMENTED,
    NN_ERROR_INVALID_PARAMETER,
    NN_ERROR_TYPE_MISMATCH,
    NN_ERROR_SHAPE_MISMATCH,
    NN_ERROR_INVALID_SHAPE,
    NN_ERROR_INVALID_ORDER,
    NN_ERROR_INVALID_AXIS,
    NN_ERROR_MISSING_RESOURCE,
    NN_ERROR_INVALID_ENGINE,
    NN_ERROR_TENSOR_NO_DATA,
    NN_ERROR_KERNEL_MISSING,
    NN_ERROR_TENSOR_TYPE_UNSUPPORTED,
    NN_ERROR_TOO_MANY_INPUTS,
    NN_ERROR_SYSTEM_ERROR,
    NN_ERROR_INVALID_LAYER,
    NN_ERROR_MODEL_INVALID,
    NN_ERROR_MODEL_MISSING,
    NN_ERROR_STRING_TOO_LARGE,
} NNError;
typedef intptr_t NNOptions;
const char*
nn_version();
const char*
nn_strerror(NNError error);
NNError
nn_init(const NNOptions* options);
typedef struct nn_engine NNEngine;
size_t
nn_engine_sizeof();
NNEngine*
nn_engine_init(void* memory);
void
nn_engine_release(NNEngine* engine);
NNError
nn_engine_load(NNEngine* engine, const char* plugin);
void
nn_engine_unload(NNEngine* engine);
const char*
nn_engine_name(NNEngine* engine);
const char*
nn_engine_version(NNEngine* engine);
typedef enum {
    NNTensorType_RAW = 0,
    NNTensorType_STR = 1,
    NNTensorType_I8 = 2,
    NNTensorType_U8 = 3,
    NNTensorType_I16 = 4,
    NNTensorType_U16 = 5,
    NNTensorType_I32 = 6,
    NNTensorType_U32 = 7,
    NNTensorType_I64 = 8,
    NNTensorType_U64 = 9,
    NNTensorType_F16 = 10,
    NNTensorType_F32 = 11,
    NNTensorType_F64 = 12
} NNTensorType;
typedef struct nn_tensor NNTensor;
size_t
nn_tensor_sizeof();
NNTensor*
nn_tensor_init(void* memory, NNEngine* engine);
void
nn_tensor_release(NNTensor* tensor);
NNEngine*
nn_tensor_engine(NNTensor* tensor);
void*
nn_tensor_native_handle(NNTensor* tensor);
void
nn_tensor_set_native_handle(NNTensor* tensor, void* handle);
typedef void(nn_aux_object_free)(NNTensor* tensor);
void
nn_tensor_set_aux_object(NNTensor* tensor,
                         void* aux_object,
                         nn_aux_object_free* aux_object_free);
void*
nn_tensor_aux_object(NNTensor* tensor);
nn_aux_object_free*
nn_tensor_aux_free(NNTensor* tensor);
void
nn_tensor_set_aux_object_by_name(NNTensor*           tensor,
                                 const char*         name,
                                 void*               aux_object,
                                 nn_aux_object_free* aux_object_free,
                                 bool                buffer_ownership,
                                 bool                name_ownership);
void*
nn_tensor_aux_object_by_name(NNTensor* tensor, const char* name);
nn_aux_object_free*
nn_tensor_aux_free_by_name(NNTensor* tensor, const char* name);
int
nn_tensor_panel_size(NNTensor* tensor);
void
nn_tensor_set_panel_size(NNTensor* tensor, int panel_size);
NNError
nn_tensor_sync(NNTensor* tensor);
int64_t
nn_tensor_time(NNTensor* tensor);
int64_t
nn_tensor_io_time(NNTensor* tensor);
void
nn_tensor_printf(NNTensor* tensor, bool data, FILE* out);
NNError
nn_tensor_assign(NNTensor* tensor,
                 NNTensorType type,
                 int32_t n_dims,
                 const int32_t shape[],
                 void* data);
NNError
nn_tensor_view(NNTensor* tensor,
               NNTensorType type,
               int32_t n_dims,
               const int32_t shape[],
               NNTensor* parent,
               int32_t offset);
NNError
nn_tensor_alloc(NNTensor* tensor,
                NNTensorType type,
                int32_t n_dims,
                const int32_t shape[]);
const int32_t*
nn_tensor_shape(const NNTensor* tensor);
const int32_t*
nn_tensor_strides(const NNTensor* tensor);
int32_t
nn_tensor_dims(const NNTensor* tensor);
const void*
nn_tensor_mapro(NNTensor* tensor);
void*
nn_tensor_maprw(NNTensor* tensor);
void*
nn_tensor_mapwo(NNTensor* tensor);
int
nn_tensor_mapped(const NNTensor* tensor);
void
nn_tensor_unmap(NNTensor* tensor);
NNTensorType
nn_tensor_type(const NNTensor* tensor);
size_t
nn_tensor_element_size(const NNTensor* tensor);
int32_t
nn_tensor_volume(const NNTensor* tensor);
int32_t
nn_tensor_size(const NNTensor* tensor);
bool
nn_tensor_shape_equal(const int32_t left[4], const int32_t right[4]);
void
nn_tensor_shape_copy(int32_t dst[4], const int32_t src[4]);
int
nn_tensor_offset(const NNTensor* tensor,
                 int32_t n_dims,
                 const int32_t shape[]);
int
nn_tensor_offsetv(const NNTensor* tensor, int32_t n_dims, ...);
int
nn_tensor_compare(NNTensor* left, NNTensor* right, double tolerance);
NNError
nn_tensor_reshape(NNTensor* tensor,
                  int32_t n_dims,
                  const int32_t shape[]);
NNError
nn_tensor_shuffle(NNTensor* output,
                  NNTensor* input,
                  int32_t n_dims,
                  const int32_t order[]);
NNError
nn_tensor_fill(NNTensor* tensor, double constant);
NNError
nn_tensor_randomize(NNTensor* tensor);
NNError
nn_tensor_copy(NNTensor* dest, NNTensor* source);
NNError
nn_tensor_concat(NNTensor* output,
                 int32_t n_inputs,
                 NNTensor* inputs[],
                 int32_t axis);
NNError
nn_tensor_slice(NNTensor* output,
                NNTensor* input,
                int32_t n_axes,
                const int32_t axes[],
                const int32_t head[],
                const int32_t tail[]);
NNError
nn_tensor_padding(NNTensor* tensor,
                  const char* padtype,
                  const int32_t* window,
                  const int32_t* stride,
                  const int32_t* dilation,
                  int32_t* padded_shape,
                  int32_t* paddings);
NNError
nn_tensor_pad(NNTensor* output,
              NNTensor* input,
              const int32_t head[4],
              const int32_t tail[4],
              double constant);
NNError
nn_tensor_load_file(NNTensor* tensor, const char* filename);
NNError
nn_tensor_load_file_ex(NNTensor* tensor, const char* filename, uint32_t proc);
NNError
nn_tensor_load_image(NNTensor* tensor, const void* image, size_t image_size);
NNError
nn_tensor_load_image_ex(NNTensor* tensor,
                        const void* image,
                        size_t image_size,
                        uint32_t proc);
NNError
nn_tensor_load_frame(NNTensor* tensor,
                     void* memory,
                     void* physical,
                     uint32_t fourcc,
                     int32_t width,
                     int32_t height,
                     const int32_t roi[4]);
NNError
nn_tensor_load_frame_ex(NNTensor* tensor,
                        void* memory,
                        void* physical,
                        uint32_t fourcc,
                        int32_t width,
                        int32_t height,
                        const int32_t roi[4],
                        uint32_t proc);
typedef void NNModel;
typedef void NNModelResource;
typedef void NNModelParameter;
typedef struct nn_context NNContext;
int
nn_model_validate(const NNModel* memory, size_t size);
const char*
nn_model_validate_error(int err);
const char*
nn_model_name(const NNModel* model);
const char*
nn_model_uuid(const NNModel* model);
uint32_t
nn_model_serial(const NNModel* model);
int
nn_model_label_count(const NNModel* model);
const char*
nn_model_label(const NNModel* model, int index);
const uint8_t*
nn_model_label_icon(const NNModel* model, int index, size_t* size);
const uint32_t*
nn_model_inputs(const NNModel* model, size_t* n_inputs);
const uint32_t*
nn_model_outputs(const NNModel* model, size_t* n_outputs);
size_t
nn_model_layer_count(const NNModel* model);
const char*
nn_model_layer_name(const NNModel* model, size_t index);
int
nn_model_layer_lookup(const NNModel* model, const char* name);
const char*
nn_model_layer_type(const NNModel* model, size_t index);
int16_t
nn_model_layer_type_id(const NNModel* model, size_t index);
const char*
nn_model_layer_datatype(const NNModel* model, size_t index);
NNTensorType
nn_model_layer_datatype_id(const NNModel* model, size_t index);
const int32_t*
nn_model_layer_zeros(const NNModel* model, size_t index, size_t* n_zeros);
const float*
nn_model_layer_scales(const NNModel* model, size_t index, size_t* n_scales);
int
nn_model_layer_axis(const NNModel* model, size_t index);
const int32_t*
nn_model_layer_shape(const NNModel* model, size_t index, size_t* n_dims);
size_t
nn_model_layer_inputs(const NNModel* model,
                      size_t index,
                      const uint32_t** inputs);
const NNModelParameter*
nn_model_layer_parameter(const NNModel* model, size_t layer, const char* key);
const int32_t*
nn_model_layer_parameter_shape(const NNModel* model,
                               size_t layer,
                               const char* key,
                               size_t* n_dims);
const float*
nn_model_layer_parameter_data_f32(const NNModel* model,
                                  size_t layer,
                                  const char* key,
                                  size_t* length);
const int16_t*
nn_model_layer_parameter_data_i16(const NNModel* model,
                                  size_t layer,
                                  const char* key,
                                  size_t* length);
const uint8_t*
nn_model_layer_parameter_data_raw(const NNModel* model,
                                  size_t layer,
                                  const char* key,
                                  size_t* length);
const char*
nn_model_layer_parameter_data_str(const NNModel* model,
                                  size_t layer,
                                  const char* key,
                                  size_t index);
size_t
nn_model_layer_parameter_data_str_len(const NNModel* model,
                                      size_t layer,
                                      const char* key);
const int32_t*
nn_model_parameter_shape(const NNModelParameter* parameter, size_t* n_dims);
const float*
nn_model_parameter_data_f32(const NNModelParameter* parameter, size_t* length);
const int32_t*
nn_model_parameter_data_i32(const NNModelParameter* parameter, size_t* length);
const int16_t*
nn_model_parameter_data_i16(const NNModelParameter* parameter, size_t* length);
const int8_t*
nn_model_parameter_data_i8(const NNModelParameter* parameter, size_t* length);
const uint8_t*
nn_model_parameter_data_raw(const NNModelParameter* parameter, size_t* length);
const char*
nn_model_parameter_data_str(const NNModelParameter* parameter, size_t index);
size_t
nn_model_parameter_data_str_len(const NNModelParameter* parameter);
size_t
nn_model_memory_size(const NNModel* model);
size_t
nn_model_cache_minimum_size(const NNModel* model);
size_t
nn_model_cache_optimum_size(const NNModel* model);
size_t
nn_model_resource_count(const NNModel* model);
const NNModelResource*
nn_model_resource_at(const NNModel* model, size_t index);
const NNModelResource*
nn_model_resource(const NNModel* model, const char* name);
const char*
nn_model_resource_name(const NNModelResource* resource);
const char*
nn_model_resource_meta(const NNModelResource* resource);
const char*
nn_model_resource_mime(const NNModelResource* resource);
const uint8_t*
nn_model_resource_data(const NNModelResource* resource, size_t* data_size);
size_t
nn_context_sizeof();
NNContext*
nn_context_init(NNEngine* engine,
                size_t memory_size,
                void* memory,
                size_t cache_size,
                void* cache);
NNContext*
nn_context_init_ex(void* context_memory,
                   NNEngine* engine,
                   size_t memory_size,
                   void* memory,
                   size_t cache_size,
                   void* cache);
void
nn_context_release(NNContext* context);
NNTensor*
nn_context_cache(NNContext* context);
NNTensor*
nn_context_mempool(NNContext* context);
NNEngine*
nn_context_engine(NNContext* context);
const NNModel*
nn_context_model(NNContext* context);
NNError
nn_context_model_load(NNContext* context,
                      size_t memory_size,
                      const void* memory);
void
nn_context_model_unload(NNContext* context);
NNTensor*
nn_context_tensor(NNContext* context, const char* name);
NNTensor*
nn_context_tensor_index(NNContext* context, size_t index);
NNError
nn_context_run(NNContext* context);
NNError
nn_context_step(NNContext* context, size_t index);
const char*
nn_context_label(const NNContext* context);
void
nn_context_outputs(const NNContext* context,
                   size_t n_outputs,
                   const NNTensor** outputs);
typedef enum {
    NNActivation_Linear = 0,
    NNActivation_ReLU = 1,
    NNActivation_ReLU6 = 2,
    NNActivation_Sigmoid = 3,
    NNActivation_SigmoidFast = 4,
    NNActivation_Tanh = 5,
} NNActivation;
typedef enum {
    NNPadding_BatchIn = 0,
    NNPadding_BatchOut = 1,
    NNPadding_Top = 2,
    NNPadding_Bottom = 3,
    NNPadding_Left = 4,
    NNPadding_Right = 5,
    NNPadding_ChannelIn = 6,
    NNPadding_ChannelOut = 7,
} NNPadding;
NNError
nn_add(NNTensor* output, NNTensor* input_a, NNTensor* input_b);
NNError
nn_subtract(NNTensor* output, NNTensor* input_a, NNTensor* input_b);
NNError
nn_multiply(NNTensor* output, NNTensor* input_a, NNTensor* input_b);
NNError
nn_divide(NNTensor* output, NNTensor* input_a, NNTensor* input_b);
NNError
nn_abs(NNTensor* output, NNTensor* input);
NNError
nn_sqrt(NNTensor* output, NNTensor* input);
NNError
nn_rsqrt(NNTensor* output, NNTensor* input, const float* epsilon);
NNError
nn_log(NNTensor* output, NNTensor* input);
NNError
nn_exp(NNTensor* output, NNTensor* input);
NNError
nn_sigmoid_fast(NNTensor* output, NNTensor* input);
NNError
nn_sigmoid(NNTensor* output, NNTensor* input);
NNError
nn_tanh(NNTensor* output, NNTensor* input);
NNError
nn_relu(NNTensor* output, NNTensor* input);
NNError
nn_relu6(NNTensor* output, NNTensor* input);
NNError
nn_prelu(NNTensor* output, NNTensor* input, NNTensor* weights);
NNError
nn_matmul(NNTensor* output,
          NNTensor* a,
          NNTensor* b,
          bool transpose_a,
          bool transpose_b);
NNError
nn_matmul_cache(NNTensor* output,
                NNTensor* cache,
                NNTensor* a,
                NNTensor* b,
                bool transpose_a,
                bool transpose_b);
NNError
nn_dense(NNTensor* output,
         NNTensor* input,
         NNTensor* weights,
         NNTensor* bias,
         NNActivation activation);
NNError
nn_linear(NNTensor* output,
          NNTensor* input,
          NNTensor* weights,
          NNTensor* bias,
          NNActivation activation);
NNError
nn_conv(NNTensor* output,
        NNTensor* cache,
        NNTensor* input,
        NNTensor* filter,
        NNTensor* bias,
        const int32_t stride[4],
        int groups,
        NNActivation activation);
NNError
nn_conv_ex(NNTensor* output,
           NNTensor* cache,
           NNTensor* input,
           NNTensor* filter,
           NNTensor* bias,
           const int32_t stride[4],
           const int32_t padding[8],
           const int32_t dilation[4],
           int groups,
           NNActivation activation);
NNError
nn_maxpool(NNTensor* output,
           NNTensor* input,
           const int32_t window[4],
           const int32_t stride[4]);
NNError
nn_maxpool_ex(NNTensor* output,
              NNTensor* input,
              const int32_t window[4],
              const int32_t stride[4],
              const int32_t padding[8],
              const int32_t dilation[4]);
NNError
nn_avgpool(NNTensor* output,
           NNTensor* input,
           const int32_t window[4],
           const int32_t stride[4]);
NNError
nn_avgpool_ex(NNTensor* output,
              NNTensor* input,
              const int32_t window[4],
              const int32_t stride[4],
              const int32_t padding[8],
              const int32_t dilation[4]);
NNError
nn_reduce_sum(NNTensor* output,
              NNTensor* input,
              int32_t n_axes,
              const int32_t axes[],
              bool keep_dims);
NNError
nn_reduce_min(NNTensor* output,
              NNTensor* input,
              int32_t n_axes,
              const int32_t axes[],
              bool keep_dims);
NNError
nn_reduce_max(NNTensor* output,
              NNTensor* input,
              int32_t n_axes,
              const int32_t axes[],
              bool keep_dims);
NNError
nn_reduce_mean(NNTensor* output,
               NNTensor* input,
               int32_t n_axes,
               const int32_t axes[],
               bool keep_dims);
NNError
nn_reduce_product(NNTensor* output,
                  NNTensor* input,
                  int32_t n_axes,
                  const int32_t axes[],
                  bool keep_dims);
NNError
nn_softmax(NNTensor* output, NNTensor* input);
NNError
nn_argmax(NNTensor* input, int* index, void* value, size_t value_size);
NNError
nn_batchnorm(NNTensor* output,
             NNTensor* cache,
             NNTensor* input,
             NNTensor* mean,
             NNTensor* variance,
             NNTensor* offset,
             NNTensor* scale,
             NNTensor* epsilon);
NNError
nn_resize(NNTensor* output,
          NNTensor* input,
          int       mode,
          bool      align_corners,
          bool      half_pixel_centers);
NNError
nn_ssd_decode_nms_standard_bbx(NNTensor* score,
                               NNTensor* trans,
                               NNTensor* anchors,
                               NNTensor* cache,
                               float     score_threshold,
                               float     iou_threshold,
                               int32_t   max_output_size_per_class,
                               NNTensor* bbx_out_tensor,
                               NNTensor* bbx_out_dim_tensor);
NNError
nn_ssd_decode_nms_variance_bbx(NNTensor* prediction,
                               NNTensor* anchors,
                               NNTensor* cache,
                               float     score_threshold,
                               float     iou_threshold,
                               int32_t   max_output_size_per_class,
                               NNTensor* bbx_out_tensor,
                               NNTensor* bbx_out_dim_tensor);
NNError
nn_ssd_nms_full(NNTensor* input,
                NNTensor* bbx_tensor,
                NNTensor* score_tensor,
                NNTensor* cache,
                float     score_threshold,
                float     iou_threshold,
                int32_t   max_output_size,
                NNTensor* bbx_out_tensor,
                NNTensor* bbx_out_dim_tensor);
typedef struct nn_gru_context NNGruContext;
NNError
nn_gru_init(NNGruContext** gru_,
            NNTensor* cache,
            NNTensorType datatype,
            int num_features,
            int num_hidden,
            int num_outputs);
void
nn_gru_release(NNGruContext* gru);
NNError
nn_gru(NNTensor* output,
       NNTensor* input,
       NNTensor* H,
       NNTensor* Wir,
       NNTensor* Bir,
       NNTensor* Wh,
       NNTensor* Bwh,
       NNTensor* Rh,
       NNTensor* Brh,
       NNGruContext* gru);
NNError
nn_svm_update_kernel(NNTensor* output,
                     NNTensor* cache,
                     NNTensor* input,
                     NNTensor* sv,
                     NNTensor* idx);
NNError
nn_svm_decision_stats(NNTensor* output,
                      NNTensor* cache,
                      NNTensor* input,
                      NNTensor* alpha,
                      NNTensor* rho);
NNError
nn_svm_soft_probability(NNTensor* output,
                        NNTensor* cache,
                        NNTensor* input,
                        NNTensor* a,
                        NNTensor* b);
void
nn_free(void* ptr);
void*
nn_malloc(size_t size);
''')


if 'DEEPVIEW_RT' in environ:
    libname = environ['DEEPVIEW_RT']

    if isdir(libname) and libname.endswith('.framework'):
        lib = ffi.dlopen(join(libname, 'Versions', 'Current', 'DeepViewRT'))
    else:
        lib = ffi.dlopen(libname)
else:
    try:
        lib = ffi.dlopen('DeepViewRT')
    except OSError:
        try:
            lib = ffi.dlopen('libdeepview-rt.so.2')
        except OSError:
            try:
                lib = ffi.dlopen('libdeepview-rt')
            except OSError:
                try:
                    lib = ffi.dlopen('deepview-rt')
                except OSError:
                    pass

if 'lib' not in locals() or lib is None:
    raise EnvironmentError('Unable to load DeepViewRT library')
