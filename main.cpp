#include <iostream>

#include <array>
#include <string>

template <typename T, size_t N>
int linearSearch(const std::array<T, N> &array, T target)
{
    for (size_t i = 0; i < array.size(); ++i)
    {
        if (array[i] == target)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    std::array<int, 7> array{1, 2, 3, 4, 5, 6, 7};
    std::array<std::string, 7> str_array{"Hello", "World", "I", "am", "here!"};

    std::cout << "Index of 'World': " << linearSearch(str_array, std::string("World")) << std::endl;
    std::cout << "Index of 3: " << linearSearch(array, 3) << std::endl;

    return 0;
}
