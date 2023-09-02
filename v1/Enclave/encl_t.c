#include "encl_t.h"

#include "sgx_trts.h" /* for sgx_ocalloc, sgx_is_outside_enclave */
#include "sgx_lfence.h" /* for sgx_lfence */

#include <errno.h>
#include <mbusafecrt.h> /* for memcpy_s etc */
#include <stdlib.h> /* for malloc/free etc */

#define CHECK_REF_POINTER(ptr, siz) do {	\
	if (!(ptr) || ! sgx_is_outside_enclave((ptr), (siz)))	\
		return SGX_ERROR_INVALID_PARAMETER;\
} while (0)

#define CHECK_UNIQUE_POINTER(ptr, siz) do {	\
	if ((ptr) && ! sgx_is_outside_enclave((ptr), (siz)))	\
		return SGX_ERROR_INVALID_PARAMETER;\
} while (0)

#define CHECK_ENCLAVE_POINTER(ptr, siz) do {	\
	if ((ptr) && ! sgx_is_within_enclave((ptr), (siz)))	\
		return SGX_ERROR_INVALID_PARAMETER;\
} while (0)

#define ADD_ASSIGN_OVERFLOW(a, b) (	\
	((a) += (b)) < (b)	\
)


typedef struct ms_enclave_generate_secret_t {
	void* ms_retval;
} ms_enclave_generate_secret_t;

typedef struct ms_enclave_destroy_secret_t {
	uint8_t* ms_cl;
} ms_enclave_destroy_secret_t;

typedef struct ms_enclave_reload_t {
	void* ms_adrs;
} ms_enclave_reload_t;

static sgx_status_t SGX_CDECL sgx_enclave_generate_secret(void* pms)
{
	CHECK_REF_POINTER(pms, sizeof(ms_enclave_generate_secret_t));
	//
	// fence after pointer checks
	//
	sgx_lfence();
	ms_enclave_generate_secret_t* ms = SGX_CAST(ms_enclave_generate_secret_t*, pms);
	sgx_status_t status = SGX_SUCCESS;



	ms->ms_retval = enclave_generate_secret();


	return status;
}

static sgx_status_t SGX_CDECL sgx_enclave_destroy_secret(void* pms)
{
	CHECK_REF_POINTER(pms, sizeof(ms_enclave_destroy_secret_t));
	//
	// fence after pointer checks
	//
	sgx_lfence();
	ms_enclave_destroy_secret_t* ms = SGX_CAST(ms_enclave_destroy_secret_t*, pms);
	sgx_status_t status = SGX_SUCCESS;
	uint8_t* _tmp_cl = ms->ms_cl;
	size_t _len_cl = 64 * sizeof(uint8_t);
	uint8_t* _in_cl = NULL;

	CHECK_UNIQUE_POINTER(_tmp_cl, _len_cl);

	//
	// fence after pointer checks
	//
	sgx_lfence();

	if (_tmp_cl != NULL && _len_cl != 0) {
		if ( _len_cl % sizeof(*_tmp_cl) != 0)
		{
			status = SGX_ERROR_INVALID_PARAMETER;
			goto err;
		}
		if ((_in_cl = (uint8_t*)malloc(_len_cl)) == NULL) {
			status = SGX_ERROR_OUT_OF_MEMORY;
			goto err;
		}

		memset((void*)_in_cl, 0, _len_cl);
	}

	enclave_destroy_secret(_in_cl);
	if (_in_cl) {
		if (memcpy_s(_tmp_cl, _len_cl, _in_cl, _len_cl)) {
			status = SGX_ERROR_UNEXPECTED;
			goto err;
		}
	}

err:
	if (_in_cl) free(_in_cl);
	return status;
}

static sgx_status_t SGX_CDECL sgx_enclave_reload(void* pms)
{
	CHECK_REF_POINTER(pms, sizeof(ms_enclave_reload_t));
	//
	// fence after pointer checks
	//
	sgx_lfence();
	ms_enclave_reload_t* ms = SGX_CAST(ms_enclave_reload_t*, pms);
	sgx_status_t status = SGX_SUCCESS;
	void* _tmp_adrs = ms->ms_adrs;



	enclave_reload(_tmp_adrs);


	return status;
}

static sgx_status_t SGX_CDECL sgx_enclave_run(void* pms)
{
	sgx_status_t status = SGX_SUCCESS;
	if (pms != NULL) return SGX_ERROR_INVALID_PARAMETER;
	enclave_run();
	return status;
}

SGX_EXTERNC const struct {
	size_t nr_ecall;
	struct {void* ecall_addr; uint8_t is_priv; uint8_t is_switchless;} ecall_table[4];
} g_ecall_table = {
	4,
	{
		{(void*)(uintptr_t)sgx_enclave_generate_secret, 0, 0},
		{(void*)(uintptr_t)sgx_enclave_destroy_secret, 0, 0},
		{(void*)(uintptr_t)sgx_enclave_reload, 0, 0},
		{(void*)(uintptr_t)sgx_enclave_run, 0, 0},
	}
};

SGX_EXTERNC const struct {
	size_t nr_ocall;
} g_dyn_entry_table = {
	0,
};


