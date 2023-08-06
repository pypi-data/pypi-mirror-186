#include <iostream>
#include <fstream>
#include <vector>
#include <cstdio>
#include <deque>

using std::cout; using std::cerr;
using std::endl; using std::string;
using std::ifstream; using std::vector;

int main(int argc, char *argv[]){
    if (argc >= 1){
        // std::cout<< argv[1];
        string filename_output(argv[1]);
        // const char * filename_output_chars = filename_output.c_str();
        string filename(argv[2]);
        // vector<char> line;
        std::deque<char> three_characters;
        char byte = 0;

        ifstream input_file(filename);
        std::ofstream output_file(filename_output);
        if (!input_file.is_open()) {
            // cerr << 'Could not open the file - '';
            //      << filename << ''' << endl;
            return EXIT_FAILURE;
        }
        // FILE * output_file;
        // output_file = fopen(filename_output_chars,"w");
        bool continue_next_line = 0;
        int current_field_index = 1;
        bool inside_string = 0;
        bool done = 0;
        int line_number = 0;
        int number_fields = 0;
        // line.clear();
        char c;
        bool is_first_command = 1;
        bool is_last_command = 0;
        bool line_finished = 0;


        while (input_file.get(byte)) {
            // std::cout << byte;
            if (three_characters.size() < 3){

              three_characters.push_back(byte);
            }else{
                char character = three_characters.front();
                three_characters.pop_front();

                if (character == ':' && three_characters.back() == ':'){
                    if (three_characters.front() == 'n'){
                        c = '\n';
                     		// fwrite(&c, sizeof(c), 1, output_file);
                        output_file.put(c);
                        three_characters.pop_front();
                        three_characters.pop_front();
                    }
                    if (three_characters.front() == 'd'){
                        c = ',';
                     		// fwrite(&c, sizeof(c), 1, output_file);
                        output_file.put(c);
                        three_characters.pop_front();
                        three_characters.pop_front();
                    }
                    if (three_characters.front() == 'r'){
                        c = '\r';
                     		// fwrite(&c, sizeof(c), 1, output_file);
                        output_file.put(c);
                        three_characters.pop_front();
                        three_characters.pop_front();
                    }
                    if (three_characters.front() == 'q'){
                        c = '\"';
                     		// fwrite(&c, sizeof(c), 1, output_file);
                        output_file.put(c);
                        three_characters.pop_front();
                        three_characters.pop_front();
                    }
                }else{
                    // fwrite(&character, sizeof(character), 1, output_file);
                    output_file.put(character);
                }
                three_characters.push_back(byte);
            }
        }
        c = three_characters.front();
        three_characters.pop_front();
        // fwrite(&c, sizeof(c), 1, output_file);
        output_file.put(c);
        c = three_characters.front();
        three_characters.pop_front();
        // fwrite(&c, sizeof(c), 1, output_file);
        output_file.put(c);


        input_file.close();
        output_file.close();
        // fclose(output_file);

        return EXIT_SUCCESS;
    }else{
        return EXIT_FAILURE;
    }
}
