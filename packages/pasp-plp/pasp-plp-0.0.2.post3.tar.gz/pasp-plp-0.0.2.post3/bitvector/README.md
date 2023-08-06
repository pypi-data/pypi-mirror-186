# Bit vector in C

Either initialize a statically allocated `bitvec_t` with an estimate `n` of number of elements
needed

```C
bitvec_t B;
if (!bitvec_init(&B, n))
  puts("Failed to allocate!");
```

or create a dynamically allocated `bitvec_t`.

```C
bitvec_t *B = bitvec_create(n);
if (!B)
  puts("Failed to allocate!");
```

Free a statically allocated `bitvec_t`

```C
bitvec_t B;
if (!bitvec_init(&B, n)) {
  /* Deal with failure. */
  ...
}
...
bitvec_free_contents(&B);
```

or a dynamically allocated `bitvec_t`.

```C
bitvec_t *B = bitvec_create(n);
if (!B) {
  /* Deal with failure. */
  ...
}
...
bitvec_free(B);
```

Given a `bitvec_t *B`, and index `size_t i`, and a `bool x`, you may set `B[i] = x`

```C
if (!bitvec_set(B, i, x))
  puts("Unable to set B[i] = x!");
```

or get `x = B[i]`.

```C
if (!bitvec_get(B, i, &x))
  puts("Unable to get x = B[i]!");
```

Likewise, you may push `x` to `B`'s tail

```C
if (!bitvec_push(B, x))
  puts("Unable to push x to B!");
```

or pop `B`'s tail.

```C
/* This operation will always succeed. */
bitvec_pop(B, &x);
```

Finally, you may print a `bitvec_t *B` with `bitvec_print`.

```C
bitvec_print(B);
```
