def generate(cfg, current_string, words):
    # verilen girdilerle bir kelime oluşturulduysa bunu yazdıralım
    if contains_only_terminals(cfg, current_string):
        words.append(current_string)
    else:
        # Kelimenin her karakterine bakalım
        for i in range(len(current_string)):
            symbol = current_string[i]
            # Eğer durum kurala uyuyorsa
            # ilgili kuralları uygulayarak yeni kelimeler üretelim.
            if symbol in cfg:
                for rule in cfg[symbol]:
                    # Yeni kelimeyi oluşturup devam edelim.
                    generated_string = current_string[:i] + rule + current_string[i + 1:]
                    generate(cfg, generated_string, words)


def contains_only_terminals(cfg, string):
    # yazılan kelimenin biizm girdilerimizle oluşup oluşmadığını kontrol edelim.
    for c in string:
        if c in cfg:
            return False
    return True


def find_duplicates(word_list):
    # Verilen kelimeler listesinde tekrarlanan kelimeleri bulalım.
    return list(filter(lambda x: word_list.count(x) > 1, set(word_list)))


def parse_cfg(cfg_input_string):
    # CFG ye gore olan toplam ağaç yapısını uyguluyoruz
    cfg = {}
    rules = cfg_input_string.split(",")
    for rule in rules:
        split_rule = rule.split("-->")
        terminal = split_rule[0].strip()
        right_hands = split_rule[1].split("|")
        cfg[terminal] = right_hands
    return cfg


def main():
    # Örnek bir CFG ifadesi
    cfg_input_string = "S-->aa|bX|aXX,X-->ab|b"
    # CFG'yi koda işleyelim
    cfg = parse_cfg(cfg_input_string)

    # Başlangıç sembolü
    starting_symbol = "S"

    # Üretilen kelimelerin tutulacağı liste
    words = []
    # Kelimeleri üret
    generate(cfg, starting_symbol, words)

    # Üretilen kelimeleri al
    distinct_words = list(set(words))
    # Üretilen kelimeleri yazdır
    print("Üretilen Kelimeler:", distinct_words)

    # Tekrarlanan kelimeleri bul
    duplicates = find_duplicates(words)
    # Tekrarlanan kelimeleri yazdır
    print("Tekrarlanan Kelimeler:", duplicates)


if __name__ == "__main__":
    main()

