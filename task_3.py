import timeit

from search.boyer_moore_search import boyer_moore_search
from search.kmp_search import kmp_search
from search.rabin_karp_search import rabin_karp_search


def read_article(filename):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == '__main__':
    article_1_content = read_article('data/article_1.txt')
    article_2_content = read_article('data/article_2.txt')

    non_existant_pattern = 'Acta non verba. Deeds, not words.'
    article_1_pattern = 'essential in software development'
    article_2_pattern = 'typically written in a step-by-step fashion'

    article_1_boyer_time_success = timeit.timeit(
        lambda: boyer_moore_search(article_1_content, article_1_pattern), number=10
    )
    article_1_boyer_time_fail = timeit.timeit(
        lambda: boyer_moore_search(article_1_content, non_existant_pattern), number=10
    )
    article_1_kmp_time_success = timeit.timeit(
        lambda: kmp_search(article_1_content, article_1_pattern), number=10
    )
    article_1_kmp_time_fail = timeit.timeit(
        lambda: kmp_search(article_1_content, non_existant_pattern), number=10
    )
    article_1_rabin_time_success = timeit.timeit(
        lambda: rabin_karp_search(article_1_content, article_1_pattern), number=10
    )
    article_1_rabin_time_fail = timeit.timeit(
        lambda: rabin_karp_search(article_1_content, non_existant_pattern), number=10
    )

    article_2_boyer_time_success = timeit.timeit(
        lambda: boyer_moore_search(article_2_content, article_2_pattern), number=10
    )
    article_2_boyer_time_fail = timeit.timeit(
        lambda: boyer_moore_search(article_2_content, non_existant_pattern), number=10
    )
    article_2_kmp_time_success = timeit.timeit(
        lambda: kmp_search(article_2_content, article_2_pattern), number=10
    )
    article_2_kmp_time_fail = timeit.timeit(
        lambda: kmp_search(article_2_content, non_existant_pattern), number=10
    )
    article_2_rabin_time_success = timeit.timeit(
        lambda: rabin_karp_search(article_2_content, article_2_pattern), number=10
    )
    article_2_rabin_time_fail = timeit.timeit(
        lambda: rabin_karp_search(article_2_content, non_existant_pattern), number=10
    )

    print(f"{'|Alogrithm': <20} | {'A1 success': <10} | {'A1 fail': <10} | {'A2 success': <10} | {'A2 fail': <10}|")
    print(f"{'|':-<20} | {'':-<10} | {'':-<10} | {'':-<10} | {'':-<10}|")

    print(f"{'|Boyer-Moore': <20} | {article_1_boyer_time_success: <10.5f} | {article_1_boyer_time_fail: <10.5f} | "
          f"{article_2_boyer_time_success: <10.5f} | {article_2_boyer_time_fail: <10.5f}|")
    print(f"{'|KMP': <20} | {article_1_kmp_time_success: <10.5f} | {article_1_kmp_time_fail: <10.5f} | "
          f"{article_2_kmp_time_success: <10.5f} | {article_2_kmp_time_fail: <10.5f}|")
    print(f"{'|Rabin-Karp': <20} | {article_1_rabin_time_success: <10.5f} | {article_1_rabin_time_fail: <10.5f} | "
          f"{article_2_rabin_time_success: <10.5f} | {article_2_rabin_time_fail: <10.5f}|")
