#ifndef ENCL_T_H__
#define ENCL_T_H__

#include <stdint.h>
#include <wchar.h>
#include <stddef.h>
#include "sgx_edger8r.h" /* for sgx_ocall etc. */


#include <stdlib.h> /* for size_t */

#define SGX_CAST(type, item) ((type)(item))

#ifdef __cplusplus
extern "C" {
#endif

void* enclave_generate_secret(void);
void enclave_destroy_secret(uint8_t cl[64]);
void enclave_reload(void* adrs);
void enclave_run(void);


#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif
