// Example program
#include <iostream>
#include <vector>
#define pii pair<int, int>
#include <set>
#include<queue>
#include<algorithm>
#include<execution>

using namespace std;

template <typename T1, typename T2> // string, int
T1 prod(T1 x, T2 times){
    T1 res = x;
    for(int i=0;i<times;i++)res += res;
    return res;
};



template <typename T, int sz>
class Array{
public:
    vector<T>array;
    T array2[sz];
    
    Array(int size){
        for(int i=0;i<size;i++)array.push_back(i);
    };
    
    Array(vector<T>fill){
        for(int i=0;i<fill.size(); i++)array[i] = fill[i];
    };
    
    void print(){
        for(auto v: array)cout<<v<<" "; cout<<endl;
    };

};


template<typename T>
class Simple{
public:
    T name, surname;
    
    Simple (T name, T surname): name(name), surname(surname)
    {
        // this->name = name;
        // this->surname = surname;
        cout<<"Intialized Name is "<<this->name<<" "<<this->surname;
        };
    void print_attrs(){
        cout<<"Name: "<<name<<" "<<surname<<endl;
    };
    
};

class Person{
public:
    string name;
    int age;
    Person(string name, int age): name(name), age(age){};
    bool operator > (const Person& other) const {
        return age > other.age;
    }; 
};

template<typename T>
void print(vector<T>& arr, string fname=""){
    if (fname.size())cout<<"Function is "<<fname<<endl;
    for(auto v: arr)cout<<v<<" "; cout<<endl;
    arr.clear();
}

int main()
{
    // algorithm examples:
    vector<int>evens{2,4,6,8};
    function<bool(int)>check_even = [](int v){return v%2==0;};
    function<bool(int)>check_odd = [](int v){return v%2 ==1;};
    
    // all_of, none_of, any_of
    auto all_even = std::all_of(evens.begin(), evens.end(), check_even);
    bool no_odds = std::none_of(evens.begin(), evens.end(), check_odd);
    // parallel execution
    bool any_odd = std::any_of(execution::par, evens.begin(), evens.end(), check_odd);
    cout<<"All even: "<<all_even<<endl<<"No odds: "<<no_odds<<endl;
    cout<<"Parallel Any odd: "<<any_odd<<endl;
    cout<<"Sum is: "<<std::reduce(evens.begin(), evens.end())<<endl;
    cout<<"Or using accumulate: "<<accumulate(evens.begin(), evens.end(), 0)<<endl ;
    
    
    // range
    vector<int>nums = {2,4, 0, 1, 8};
    vector<int>evens_new;
    
    // transform and make different array
    transform(nums.begin(), nums.end(), back_inserter(evens_new), [](int v){return v*2;});
    print(evens_new, "transform");
    
    //for_each
    vector<int>nc (nums);
    for_each(nc.begin(), nc.end(), [](int &v){v++;});
    print(nc, "for_each");
    
    // count
    cout<<"count 2: "<<count(nums.begin(), nums.end(), 2)<<endl;
    
    
    // count_if
    cout<<"count even: "<<count_if(nums.begin(), nums.end(), [](int v){return int(v%2) == 0;})<<endl;
    
    // find
    auto it = find(nums.begin(), nums.end(), 4);
    cout<<"Find 4:"<<" *it= "<< *it <<" or nums[it-nums.begin()]= "<<nums[it-nums.begin()]<<endl;; 
    
    //find_if
    auto it1 = find_if(nums.begin(), nums.end(), [](int v){return v%2 == 0;});
    cout<<"First even:"<<" *it= "<< *it1 <<" or nums[it-nums.begin()]= "<<nums[it1-nums.begin()]<<endl;; 
    
    
    //fill
    evens_new.resize(5,0);
    fill (evens_new.begin(),evens_new.begin()+3,7);
    print(evens_new, "fill");
    
    // fill_n
    fill_n(back_inserter(evens_new), 3, -1); // fill 3 times -1.
    print(evens_new, "fill_n");
    
    //copy
    copy(nums.begin(), nums.end(), back_inserter(evens_new)); // back_inserter inserts like push_back
    print(evens_new, "copy");
    
    // copy_if
    copy_if(nums.begin(), nums.end(), back_inserter(evens_new), [](int v){ return int (v%2) == 0 ;});
    auto is_even = ranges::all_of(evens_new, [](int v){return int(v%2) == 0;});
    cout<<"All even: "<<is_even<<endl;
    print(evens_new);
    
}
