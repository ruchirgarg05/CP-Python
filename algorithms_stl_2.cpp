/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

template<typename T>
void print(vector<T>&A, string name=""){
    if (name.size())cout<<"Function is "<<name<<" \n";
    for(auto a: A)cout<<a<<" "; cout<<"\n";
    A.clear();
}
int main()
{
    vector<int> v(5,0);
    int i=1;
    // for_each_n
    for_each_n(v.begin(), 3, [&](int& val){val = i*i; i++;});
    print(v, "for_each_n");
    
    v.resize(5);
    //iota
    iota(v.begin(), v.end(), 0);
    print(v, "iota");
    
    // // copy_backward
    
    v.resize(5); 
    iota(v.begin(), v.end(), 0);
    vector<int>dest(7,0);
    
    copy_backward(v.begin(), v.end(), dest.end());
    print(dest, "copy_backward");

    // copy_n
    dest.resize(10);
    copy_n(v.cbegin(), 5, dest.begin()); // copy_5
    print(dest, "copy_n"); 
    
    dest.resize(9);
    copy(v.cbegin(), v.cend(), dest.begin()); // back_inserter inserts in the back.
    print(dest, "copy");
    
    //accumulate
    
    string acc = accumulate(next(v.begin()), v.end(),
                          to_string(v[0]), 
                          [](string a, int b){
                              return a + ", " + to_string(b); }) ; // return dash separated string 
    
    cout<<"Accumulated value: "<<acc<<endl;
    
    // inner product
    vector<int>a1(10, 0), b1(10, 0);
    int cnt = 4;
    iota(b1.begin(), b1.end(), 0);
    iota(a1.begin(), a1.end(), 0);
    cout<<"B is : ";
    for_each(b1.begin(), b1.end(), [](auto v){cout<<v<<" ";});
    cout<<"Inner product of first "<<cnt<<" indexes are: "<<
           inner_product(a1.begin(), a1.begin()+cnt, b1.begin(), 0)<<endl;
           
    // Prefix_sum
    vector<int>prefix_sum(10,0);
    iota(prefix_sum.begin(), prefix_sum.end(), 0);
    partial_sum(prefix_sum.begin(), prefix_sum.end(), prefix_sum.begin(), 
                [](int sum_till_now, int val){return sum_till_now + 2*val;}); // prefix_sum = prefix_sum + 2*nums[i];
    print(prefix_sum, "partial_sum/ prefix_sum");
    
    
    
                         
    
    return 0;
}
