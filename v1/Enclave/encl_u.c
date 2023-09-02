#include "encl_u.h"
#include <errno.h>

typedef struct ms_enclave_generate_secret_t {
	void* ms_retval;
} ms_enclave_generate_secret_t;

typedef struct ms_enclave_destroy_secret_t {
	uint8_t* ms_cl;
} ms_enclave_destroy_secret_t;

typedef struct ms_enclave_reload_t {
	void* ms_adrs;
} ms_enclave_reload_t;

static const struct {
	size_t nr_ocall;
	void * table[1];
} ocall_table_encl = {
	0,
	{ NULL },
};
sgx_status_t enclave_generate_secret(sgx_enclave_id_t eid, void** retval)
{
	sgx_status_t status;
	ms_enclave_generate_secret_t ms;
	status = sgx_ecall(eid, 0, &ocall_table_encl, &ms);
	if (status == SGX_SUCCESS && retval) *retval = ms.ms_retval;
	return status;
}

sgx_status_t enclave_destroy_secret(sgx_enclave_id_t eid, uint8_t cl[64])
{
	sgx_status_t status;
	ms_enclave_destroy_secret_t ms;
	ms.ms_cl = (uint8_t*)cl;
	status = sgx_ecall(eid, 1, &ocall_table_encl, &ms);
	return status;
}

sgx_status_t enclave_reload(sgx_enclave_id_t eid, void* adrs)
{
	sgx_status_t status;
	ms_enclave_reload_t ms;
	ms.ms_adrs = adrs;
	status = sgx_ecall(eid, 2, &ocall_table_encl, &ms);
	return status;
}

sgx_status_t enclave_run(sgx_enclave_id_t eid)
{
	sgx_status_t status;
	status = sgx_ecall(eid, 3, &ocall_table_encl, NULL);
	return status;
}

