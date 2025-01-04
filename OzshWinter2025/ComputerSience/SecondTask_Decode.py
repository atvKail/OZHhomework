import sys


def read_input(file_path):
    with open(file_path, "r") as file:
        k = int(file.readline().strip())
        s = file.readline().strip()
    return k, s


def write_output(file_path, result):
    with open(file_path, "w") as file:
        file.write(result)


def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(1, n + 1) if is_prime[i]]


def decrypt_message(k, encrypted_message):
    n = len(encrypted_message)
    primes = sieve_of_eratosthenes(n)
    for _ in range(k):
        prime_positions = [p - 1 for p in primes if p <= n]
        non_prime_positions = [i for i in range(n) if i not in prime_positions]

        temp_message = list(encrypted_message)

        first_block = encrypted_message[: len(prime_positions)]
        second_block = encrypted_message[len(prime_positions) :]

        for i, pos in enumerate(prime_positions):
            temp_message[pos] = first_block[i]
        for i, pos in enumerate(non_prime_positions):
            temp_message[pos] = second_block[i]

        encrypted_message = "".join(temp_message)

    return encrypted_message


def main():
    input_file = sys.path[0] + "/" + "input.txt"
    output_file = sys.path[0] + "/" + "output.txt"

    k, encrypted_message = read_input(input_file)
    decrypted_message = decrypt_message(k, encrypted_message)

    write_output(output_file, decrypted_message)


if __name__ == "__main__":
    main()


# Использую: sys.path[0] + "/" + для input.txt и output.txt
