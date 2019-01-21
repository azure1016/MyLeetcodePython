#include <iostream>
#include <string>

class Solution{
public:
    void reverse(char *str){
        char tmp = '\0';
        int len = sizeof(*str);
        if (len == 0 || len == 1) return;
        int mid = len / 2;
        for (int i = 0; i < mid; i++){
            tmp = *(str);
            *str = *(str + len - i - 1);
            *(str + len - i - 1) = tmp;
        }
    }
};

int main(int argc, const char * argv[]) {
    Solution test;
    char s[5] = {'q', 'u', 'i', 't', '\0'};
    test.reverse(s);
    std::cout << s << std::endl;
    return 0;
}
