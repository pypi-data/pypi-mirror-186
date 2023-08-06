#include <stdio.h>
#include <limits.h>
#include <string.h>

#include "bitvector.h"

#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))

/* Bit operations. */
#define BIT_SET(b, i, x) b = ((b) & ~(1ULL << (i))) | (((unsigned long long int) (x)) << (i))
#define BIT_GET(b, i) (((b) >> (i)) & 1ULL)
#define ONES_UP_TO(i) (~0ULL >> (ULL_BIT_SIZE-(i)))

/* Out of bounds. */
#define OOB(B, i,  b) (((i) >= (B)->n) || ((b) >= (B)->c))

typedef unsigned long long int ull_t;
const size_t ULL_BIT_SIZE = sizeof(ull_t)*8;
const size_t ULL_BIT_SIZE_M = sizeof(ull_t)*8-1;

bool bitvec_init(bitvec_t *B, size_t n) {
  size_t b = n/ULL_BIT_SIZE + 1;
  B->n = 0;
  B->c = max(1, b);
  B->d = (ull_t*) calloc(b, sizeof(ull_t));
  if (!B->d) return false;
  return true;
}

bitvec_t* bitvec_create(size_t n) {
  size_t b = n/ULL_BIT_SIZE;
  bitvec_t *B = (bitvec_t*) malloc(sizeof(bitvec_t));
  if (!B) return NULL;
  B->n = 0;
  B->c = max(1, b);
  B->d = (ull_t*) calloc(b, sizeof(ull_t));
  if (!B->d) { free(B); return NULL; }
  return B;
}

bitvec_t* bitvec_zero(bitvec_t *B) { bitvec_fill(B); memset(B->d, 0, B->c*sizeof(ull_t)); return B; }
bitvec_t* bitvec_one(bitvec_t *B) { bitvec_fill(B); memset(B->d, -1, B->c*sizeof(ull_t)); return B; }
bitvec_t* bitvec_fill(bitvec_t *B) { B->n = B->c*ULL_BIT_SIZE; return B; }
bitvec_t* bitvec_filln(bitvec_t *B, size_t n) { B->n = n; return B; }
bitvec_t* bitvec_zeron(bitvec_t *B, size_t n) {
  bitvec_filln(B, n);
  memset(B->d, 0, ((B->n/ULL_BIT_SIZE) + 1)*sizeof(ull_t));
  return B;
}
bitvec_t* bitvec_onen(bitvec_t *B, size_t n) {
  bitvec_filln(B, n);
  memset(B->d, -1, ((B->n/ULL_BIT_SIZE) + 1)*sizeof(ull_t));
  return B;
}

bitvec_t* bitvec_copy(bitvec_t *src, bitvec_t *dst) {
  size_t i;
  if (!dst) {
    dst = (bitvec_t*) malloc(sizeof(bitvec_t));
    if (!dst) goto error;
    dst->d = (ull_t*) calloc(src->c, sizeof(ull_t));
    if (!dst->d) { free(dst); goto error; }
    dst->c = src->c;
  } else if (dst->c < src->c) {
    ull_t *p;
    p = (ull_t*) realloc(dst->d, src->c*sizeof(ull_t));
    if (!p) goto error;
    dst->d = memset(p, 0, src->c*sizeof(ull_t));
    dst->c = src->c;
  }
  dst->n = src->n;
  for (i = 0; i <= (src->n / ULL_BIT_SIZE); ++i)
    dst->d[i] = src->d[i];
  return dst;
error:
  return NULL;
}

void bitvec_free_contents(bitvec_t *B) { free(B->d); B->d = NULL; B->n = B->c = 0; }
void bitvec_free(bitvec_t *B) { bitvec_free_contents(B); free(B); }

bool bitvec_set(bitvec_t *B, size_t i, bool x) {
  size_t b = i/ULL_BIT_SIZE, j = i%ULL_BIT_SIZE;
  if (OOB(B, i, b)) return false;
  BIT_SET(B->d[b], j, x);
  return true;
}
bool bitvec_get(bitvec_t *B, size_t i, bool *x) {
  size_t b = i/ULL_BIT_SIZE, j = i%ULL_BIT_SIZE;
  if (OOB(B, i, b)) return false;
  *x = BIT_GET(B->d[b], j);
  return true;
}

void bitvec_SET(bitvec_t *B, size_t i, bool x) {
  register size_t b = i/ULL_BIT_SIZE, j = i%ULL_BIT_SIZE;
  BIT_SET(B->d[b], j, x);
}
bool bitvec_GET(bitvec_t *B, size_t i) {
  register size_t b = i/ULL_BIT_SIZE, j = i%ULL_BIT_SIZE;
  return BIT_GET(B->d[b], j);
}

#define MAGIC_ADD_LEN 2

bool bitvec_grow(bitvec_t *B) {
  ull_t *d;
  d = (ull_t*) realloc(B->d, (B->c+MAGIC_ADD_LEN)*sizeof(ull_t));
  if (!d) return false;
  B->d = d;
  B->c += MAGIC_ADD_LEN;
  return true;
}

bool bitvec_push(bitvec_t *B, bool x) {
  size_t i = B->n;
  size_t b = i/ULL_BIT_SIZE, j = i%ULL_BIT_SIZE;
  if (B->n % ULL_BIT_SIZE == ULL_BIT_SIZE_M) if (!bitvec_grow(B)) return false;
  ++B->n;
  BIT_SET(B->d[b], j, x);
  return true;
}
bool bitvec_pop(bitvec_t *B, bool *x) {
  size_t i = --B->n;
  size_t b = i/ULL_BIT_SIZE, j = i%ULL_BIT_SIZE;
  if (!x) return true;
  *x = BIT_GET(B->d[b], j);
  return true;
}

bool bitvec_cmp(bitvec_t *A, bitvec_t *B) {
  size_t i, n = A->n;
  size_t l = n / ULL_BIT_SIZE, r = n % ULL_BIT_SIZE;
  if (n != B->n) return false;
  for (i = 0; i < l; ++i)
    if (A->d[i] != B->d[i]) return false;
  if (r == 0) return true;
  ull_t m = ONES_UP_TO(r);
  if ((A->d[i] & m) != (B->d[i] & m)) return false;
  return true;
}

void print_ull(unsigned long long int d, size_t k) {
  size_t i;
  putchar('|');
  for (i = 0; i < k; ++i) putchar('0' + ((d >> i) & 1ULL));
}

void bitvec_print(bitvec_t *B) {
  size_t i;
  printf("<[");
  for (i = 0; i < B->n; i += ULL_BIT_SIZE) print_ull(B->d[i/ULL_BIT_SIZE], (i+ULL_BIT_SIZE > B->n)*(B->n - i) + (i+ULL_BIT_SIZE <= B->n)*ULL_BIT_SIZE);
  printf("|],\nn = %lu, c = %lu, c*%lu = %lu>\n", B->n, B->c, ULL_BIT_SIZE, B->c*ULL_BIT_SIZE);
}

bool bitvec_incr(const bitvec_t *B) {
  size_t i, n = B->n / ULL_BIT_SIZE, r = B->n % ULL_BIT_SIZE;
  bool carry = true;
  for (i = 0; carry && i < n; ++i) {
    carry = B->d[i] == ULLONG_MAX;
    ++B->d[i];
  }
  if (!carry || (r == 0)) return !carry;
  carry = B->d[i] == ONES_UP_TO(r);
  B->d[i] = carry*0 + (!carry)*(B->d[i]+1); /* if carry, then 0; otherwise increment. */
  return !carry;
}
