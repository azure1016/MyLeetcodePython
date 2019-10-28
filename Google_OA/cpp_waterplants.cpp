#include <iostream>
#include <vector>
#include <algorithm>

int findSteps(const vector<int> &input, int capacity)
{
    int steps = 0;
    int cap = capacity;
    int maxElement = *max_element(input.begin(), input.end());
    if (maxElement > capacity)
        return -1;
    for (int i = 0; i < input.size(); ++i)
    {
        if (input[i] <= cap)
        {
            cap -= input[i];
        }
        else
        {
            steps += (2 * i);
            cap = capacity - input[i];
        }
        ++steps;
    }
    return steps;
}

void main() {
    int plants[] = {1,2,3,4,5,1,2,3,4,5,3,4,5,5,3,3,2,2,4,5,6,6,7,4,5,4,3,5,6,7,8,8,6,4,5,4,4,5,4,6,7,9};
    vector<int>
    int res = findSteps(plants, 10);
    std::cout>>(res);

}