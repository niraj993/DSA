def reverse_an_string(string:str)->str:
    reverse = ""
    for i in range(len(string)-1,-1,-1):
        reverse+=string[i]
    return reverse

def check_panindrome(string:str)->str:
    reversed_str = reverse_an_string(string=string)
    return reversed_str == string


def count_vowel_and_const(string:str)->int:
    vowels = 0
    const = 0
    vowel_hash = {
        "a" : 1,
        "e" : 2,
        "i" :3,
        "o" : 4,
        "u" : 5
    }
    for i in range(0,len(string)):
        if string[i] in vowel_hash:
            vowels+=1
        else:
            const +=1
    return (vowels,const)

def count_freq_of_char(string:str)->int:
    hash_map = {}
    for i in range(0,len(string)):
        hash_map[string[i]] = hash_map.get(string[i],0) + 1
    return hash_map

def remove_duplicate_char(string:str)->str:
    n = len(string)
    freq_map = {}
    for i in range(0,n):
        freq_map[string[i]] = 1
    
    result = ""
    for j in freq_map:
        result += j
    return result
        
def check_anagram(str_1:str,str_2:str)->bool:
    freq_map_str1 = {}
    freq_map_str2 = {}
    for i in range(0,len(str_1)):
        freq_map_str1[str_1[i]] = freq_map_str1.get(str_1[i],0) + 1
    
    for j in range(0,len(str_2)):
        freq_map_str2[str_2[j]] = freq_map_str2.get(str_2[j],0) + 1
    
    return freq_map_str1 == freq_map_str2


def find_first_non_repeating_charter(string:str)->str:
    freq_map = {}
    for i in range(0,len(string)):
        freq_map[string[i]] = freq_map.get(string[i],0) + 1
    
    for key in freq_map:
        if freq_map[key] == 1:
            return key
    

def find_first_repeating_charter(string:str)->str:
    freq_map = {}
    for i in range(0,len(string)):
        freq_map[string[i]] = freq_map.get(string[i],0) + 1
    
    for key in freq_map:
        if freq_map[key] == 2:
            return key

def reverse_word_in_sentence(string:str)->List[str]:
    result = []
    for word in string.split():
        result.append(word[::-1])
    return result


def remove_white_space(string:str)->str:
    result = ""
    for i in string:
        if i != " ":
            result += i
    return result

def capitalize_first_letter_of_each_word(string:List[str])->str:
    result = []
    for word in string:
        first_word_cap = word[0].upper() + word[1:]
        result.append(first_word_cap)
    return result

def find_length_without_len(string:str)->int:
    count = 0
    for _ in string:
        count+=1
    return count

def print_duplicate_char(string:str)->int:
    freq_map = {}
    for ch in string:
        freq_map[ch] = freq_map.get(ch,0) + 1
    
    result = []
    for key in freq_map:
        if freq_map[key] == 2:
            result.append(key)
    return result




result = print_duplicate_char(string="nname")
print("============>",result)
