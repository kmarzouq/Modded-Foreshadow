#ifndef ENCL_U_H__
#define ENCL_U_H__

#include <stdint.h>
#include <wchar.h>
#include <stddef.h>
#include <string.h>
#include "sgx_edger8r.h" /* for sgx_status_t etc. */


#include <stdlib.h> /* for size_t */

#define SGX_CAST(type, item) ((type)(item))

#ifdef __cplusplus
extern "C" {
#endif


sgx_status_t enclave_generate_secret(sgx_enclave_id_t eid, void** retval);
sgx_status_t enclave_destroy_secret(sgx_enclave_id_t eid, uint8_t cl[64]);
sgx_status_t enclave_reload(sgx_enclave_id_t eid, void* adrs);
sgx_status_t enclave_run(sgx_enclave_id_t eid);

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif
