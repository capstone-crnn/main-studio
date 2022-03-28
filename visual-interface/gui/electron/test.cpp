#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstring>
#include <cstddef>
#include <cstdlib>

#include <vector>

using namespace std;
int main(int argc, char *argv[])
{



   //Define file names
   const char *FileName  = "bpm_data";
   const std::size_t FileSize = 10000;
   vector<int> rates(3);
   rates[0] = 14;
   rates[1] = 60;
   rates[2] = 1;

	int count = 0;
	for(int i=0; ; i++){
		
		ofstream myfile;
		myfile.open (FileName, ios::in | ios::out | ios::trunc | ios::binary);
		myfile << count << " \n";
		std::cout << count << "\n";
		
		myfile.close();

		count++;

	}
	return 0;
}
