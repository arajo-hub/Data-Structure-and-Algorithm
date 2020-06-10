# Hash Table은 해싱 함수에 의하여 참조되는 테이블을 말한다.

hash_table=[[] for _ in range(10)]
print(hash_table)

def insert(hash_table, key, value):
    hash_key=(key%len(hash_table))

    key_exists=False
    bucket=hash_table[hash_key]

    for i, kv in enumerate(bucket):

        k, v= kv
        if key==k:
            key_exists=True
            break
    if key_exists:
        bucket[i]=((key, value))
    else:
        bucket.append((key, value))