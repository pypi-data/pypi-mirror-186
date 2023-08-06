#include <iostream>
#include <fstream>
#include <vector>
#include <cstdio>
#include <deque>
#include <string>

using std::cerr;
using std::endl; using std::string;
using std::ifstream; using std::vector;



int main(int argc, char *argv[]){
  std::ios_base::sync_with_stdio(false);
    if (argc >= 1){
        // //std::cout<< argv[1];
        string filename(argv[1]);
        // vector<char> line;
        std::deque<char> two_characters;
        char byte = 0;

        std::vector<std::string> nans;
        nans.push_back("#N/A");
        nans.push_back("#N/A");
        nans.push_back("N/A");
        nans.push_back("#NA");
        nans.push_back("-1.#IND");
        nans.push_back("-1.#QNAN");
        nans.push_back("-NaN");
        nans.push_back("-nan");
        nans.push_back("1.#IND");
        nans.push_back("1.#QNAN");
        nans.push_back("<NA>");
        nans.push_back("<na>");
        nans.push_back("N/A");
        nans.push_back("NA");
        nans.push_back("NULL");
        nans.push_back("NaN");
        nans.push_back("n/a");
        nans.push_back("nan");
        nans.push_back("null");
        nans.push_back("");
        nans.push_back("Nan");
        nans.push_back("-Nan");

        ifstream input_file(filename);
        if (!input_file.is_open()) {
            // cerr << 'Could not open the file - '';
            //      << filename << ''' << endl;
            return EXIT_FAILURE;
        }

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
        // bool accumulating = false;
        std::string result_accumulation = "";
        //std::cout << "starting" << '\n';

        while (input_file.get(byte)) {
            // //std::cout << byte;
            if (two_characters.size() < 2){

              two_characters.push_back(byte);
            }else{
                char character = two_characters.front();
                two_characters.pop_front();
                two_characters.push_back(byte);
                // while (!done){



                    // for (i=1;i<=length($0);i++){
                // int counter = 0;
                if (character == '\n' || input_file.eof()){
                    line_finished = 1;
                }else{
                    line_finished = 0;

                    // counter++;
                    if (inside_string){
                        if ((is_first_command) && (!is_last_command) && (character == ',')){
                            c = ':';
    												fwrite(&c, sizeof(c), 1, stdout );
                            c = 'd';
    												fwrite(&c, sizeof(c), 1, stdout );
                            c = ':';
    												fwrite(&c, sizeof(c), 1, stdout );
                        }else if ((is_first_command) && (!is_last_command) && (character == '\r')){
                            c = ':';
    												fwrite(&c, sizeof(c), 1, stdout );
                            c = 'r';
    												fwrite(&c, sizeof(c), 1, stdout );
                            c = ':';
    												fwrite(&c, sizeof(c), 1, stdout );
                        }else if (is_first_command && !is_last_command && (character == '\"') && ((two_characters.front() != '\n' && two_characters.front() != ',') && !(two_characters.front() == '\r' && two_characters.back() == '\n'))){
                            c = ':';
    												fwrite(&c, sizeof(c), 1, stdout );
                            c = 'q';
    												fwrite(&c, sizeof(c), 1, stdout );
                            c = ':';
    												fwrite(&c, sizeof(c), 1, stdout );
                        }else{
                            fwrite(&character, sizeof(character), 1, stdout );
                        }
                        if (character == '\"' && (two_characters.front() == '\n' || two_characters.front() == ',' || (two_characters.front() == '\r' && two_characters.back() == '\n'))){
                            inside_string = 0;
                        }
                    }else{
                        if (character == '\"'){
                            inside_string = 1;
                            fwrite(&character, sizeof(character), 1, stdout );
                        }else{                            
                            if (character == ',' || two_characters.front() == '\n'){
                              //std::cout << "A" << '\n';
                                if (two_characters.front() == '\n' && character == ','){
                                  //std::cout << "A.1" << '\n';
                                  if (result_accumulation.size() == 0){
                                    if (character != '\r'){
                                      fwrite(&character, sizeof(character), 1, stdout );
                                    }
                                  }else{
                                    int length = result_accumulation.size();
                                    bool is_nan = false;
                                    for(int i=0;i<nans.size();i++){
                                      is_nan = is_nan || result_accumulation == nans[i];
                                      if (is_nan){
                                        break;
                                      }
                                    }

                                    if (is_nan){
                                        result_accumulation = "";
                                    }else{
                                      for (char char_ : result_accumulation){
                                        if (char_ != '\r'){
                                          fwrite(&char_, sizeof(char_), 1, stdout );
                                        }
                                      }
                                      result_accumulation = "";

                                    }
                                    if (character != '\r'){
                                      fwrite(&character, sizeof(character), 1, stdout );
                                    }
                                  }
                                    // fields[current_field_index] = field;
                                    // field = '';
                                    current_field_index += 1;
                                    // fields[current_field_index] = '';
                                }
                                else if (two_characters.front() == '\n'){
                                  //std::cout << "A.2" << '\n';
                                  if (result_accumulation.size() == 0){
                                    //std::cout << "A.2.A" << '\n';
                                    //std::cout<<character<<'\n';
                                    if (character != '\r'){
                                      fwrite(&character, sizeof(character), 1, stdout );
                                    }
                                  }else{
                                    //std::cout << "A.2.B" << " " << character<<" "<<result_accumulation.size() << '\n';
                                    // //std::cout<<character<<" "<<two_characters.front()<<'\n';
                                    result_accumulation.push_back(character);                                    
                                    int length = result_accumulation.size();
                                    bool is_nan = false;
                                    for(int i=0;i<nans.size();i++){
                                      is_nan = is_nan || result_accumulation == nans[i];
                                      if (is_nan){
                                        break;
                                      }
                                    }

                                    if (is_nan){
                                        result_accumulation = "";
                                    }else{
                                      for (char char_ : result_accumulation){
                                        if (char_ != '\r'){
                                          fwrite(&char_, sizeof(char_), 1, stdout );
                                        }
                                      }
                                      result_accumulation = "";
                                      if (character != '\r'){
                                        fwrite(&character, sizeof(character), 1, stdout );
                                      }

                                    }
                                    
                                  }
                                    // fields[current_field_index] = field;
                                    // field = '';

                                }else{
                                  //std::cout << "A.3" << '\n';
                                  
                                  if (result_accumulation.size() == 0){
                                    if (character != '\r'){
                                      fwrite(&character, sizeof(character), 1, stdout );
                                    }
                                  }else{
                                    int length = result_accumulation.size();
                                    bool is_nan = false;
                                    for(int i=0;i<nans.size();i++){
                                      is_nan = is_nan || result_accumulation == nans[i];
                                      if (is_nan){
                                        break;
                                      }
                                    }

                                    if (is_nan){
                                        result_accumulation = "";
                                    }else{
                                      for (char char_ : result_accumulation){
                                        if (char_ != '\r'){
                                          fwrite(&char_, sizeof(char_), 1, stdout );
                                        }
                                      }
                                      result_accumulation = "";

                                    }
                                    if (character != '\r'){
                                      fwrite(&character, sizeof(character), 1, stdout );
                                    }
                                  }
                                    // fields[current_field_index] = field;
                                    // field = '';
                                    current_field_index += 1;

                                }


                            }else{
                              //std::cout << "C"<<" "<< character<<" "<<result_accumulation.size()<<'\n';
                              if (result_accumulation.size() == 0){
                                bool is_nan = false;
                                int length = 1;
                                for(int i=0;i<nans.size();i++){
                                  is_nan = is_nan || (length <= nans[i].size() && character == nans[i].at(0));
                                  if (is_nan){
                                    break;
                                  }
                                }

                                if (is_nan){
                                  result_accumulation.push_back(character);

                                }else{
                                    if (character != '\r'){
                                      fwrite(&character, sizeof(character), 1, stdout );
                                    }
                                }
                              }else{
                                result_accumulation.push_back(character);
                                int length = result_accumulation.size();

                                bool is_nan = false;
                                for(int i=0;i<nans.size();i++){
                                  is_nan = is_nan || (length <= nans[i].size() && result_accumulation == nans[i].substr(0,length));
                                  if (is_nan){
                                    break;
                                  }
                                }

                                if (is_nan){

                                }else{
                                  for (char char_ : result_accumulation){
                                      if (char_ != '\r'){
                                        fwrite(&char_, sizeof(char_), 1, stdout );
                                      }
                                  }
                                  result_accumulation = "";

                                }

                              }
                                // fwrite(&character, sizeof(character), 1, stdout );
                            }
                        }

                    }
                  }

                // }
                if (line_finished){
                    if (line_number == 0){
                        // field = '';
                        // for (i=1;i<=current_field_index;i++){
                        //     $i = fields[i];
                        // }
                        // NF = current_field_index;
                        // $1 = $1;
                        number_fields = current_field_index;
                        continue_next_line = 0;
                        done = 1;
                        line_number++;
                    }else{
                        if (inside_string){
                            continue_next_line = 1;
                            // records_skipped += 1;
                            done = 0;
                        }
                        if (number_fields > current_field_index){
                            continue_next_line = 1;
                            // records_skipped += 1;
                            done = 0;
                        }else{
                            continue_next_line = 0;
                            // field = '';
                            // for (i=1;i<=current_field_index;i++){
                            //     $i = fields[i];
                            // }
                            // NF = current_field_index;
                            // $1 = $1;
                            done = 1;
                            line_number++;
                        }
                    }

                    if (!continue_next_line){
                        current_field_index = 1;
                        inside_string = 0;
                        // for (char i : line) {
                        //     // //std::cout << i;
                        //     fwrite(&i, sizeof(i), 1, stdout );
                        // }
                        char c = '\n';
                        fwrite(&c, sizeof(c), 1, stdout );
                        // //std::cout<<'\n';
                        // //std::cout<< line.size();
                        // cout << endl;

                        // cout << &line;
                        // line.clear();
                        // field = '';
                    }else{
                        c = ':';
    										fwrite(&c, sizeof(c), 1, stdout );
                        c = 'n';
    										fwrite(&c, sizeof(c), 1, stdout );
                        c = ':';
    										fwrite(&c, sizeof(c), 1, stdout );
                    }
                }

                // }

            }

        }
        char character = two_characters.front();
        if (inside_string){
            if ((is_first_command) && (!is_last_command) && (character == ',')){
                c = ':';
                fwrite(&c, sizeof(c), 1, stdout );
                c = 'd';
                fwrite(&c, sizeof(c), 1, stdout );
                c = ':';
                fwrite(&c, sizeof(c), 1, stdout );
            }else if ((is_first_command) && (!is_last_command) && (character == '\r')){
                c = ':';
                fwrite(&c, sizeof(c), 1, stdout );
                c = 'r';
                fwrite(&c, sizeof(c), 1, stdout );
                c = ':';
                fwrite(&c, sizeof(c), 1, stdout );
            }else if (is_first_command && !is_last_command && (character == '\"') && (two_characters.front() != '\n' && two_characters.front() != ',')){
                c = ':';
                fwrite(&c, sizeof(c), 1, stdout );
                c = 'q';
                fwrite(&c, sizeof(c), 1, stdout );
                c = ':';
                fwrite(&c, sizeof(c), 1, stdout );
            }else{
                fwrite(&character, sizeof(character), 1, stdout );
            }
            if (character == '\"' && (two_characters.front() == '\n' || two_characters.front() == ',')){
                inside_string = 0;
            }
        }else{
            if (character == '\"'){
                inside_string = 1;
                fwrite(&character, sizeof(character), 1, stdout );
            }else{
                if (character == ',' || two_characters.front() == '\n'){
                  //std::cout<<"last-A"<<'\n';
                    if (two_characters.front() == '\n' && character == ','){
                      //std::cout<<"last-A1"<<'\n';
                        fwrite(&character, sizeof(character), 1, stdout );
                        // fields[current_field_index] = field;
                        // field = '';
                        current_field_index += 1;
                        // fields[current_field_index] = '';
                    }
                    else if (two_characters.front() == '\n'){
                        //std::cout<<"last-A2"<<'\n';
                        if (character != '\r'){
                          fwrite(&character, sizeof(character), 1, stdout );
                        }
                        // fields[current_field_index] = field;
                        // field = '';

                    }else{
                      //std::cout<<"last-A3"<<'\n';
                        if (character != '\r'){
                          fwrite(&character, sizeof(character), 1, stdout );
                        }
                        // fields[current_field_index] = field;
                        // field = '';
                        current_field_index += 1;

                    }


                }else{
                  //std::cout<<"last-B"<<'\n';
                    // if (character != '\r'){
                    //   fwrite(&character, sizeof(character), 1, stdout );
                    // }
                    if (result_accumulation.size() == 0){
                      //std::cout << "A.2.A" << '\n';
                      //std::cout<<character<<'\n';
                      if (character != '\r'){
                        fwrite(&character, sizeof(character), 1, stdout );
                      }
                    }else{
                      //std::cout << "A.2.B" << " " << character<<" "<<result_accumulation.size() << '\n';
                      // //std::cout<<character<<" "<<two_characters.front()<<'\n';
                      result_accumulation.push_back(character);                                    
                      int length = result_accumulation.size();
                      bool is_nan = false;
                      for(int i=0;i<nans.size();i++){
                        is_nan = is_nan || result_accumulation == nans[i];
                        if (is_nan){
                          break;
                        }
                      }

                      if (is_nan){
                          result_accumulation = "";
                      }else{
                        for (char char_ : result_accumulation){
                          if (char_ != '\r'){
                            fwrite(&char_, sizeof(char_), 1, stdout );
                          }
                        }
                        result_accumulation = "";
                        if (character != '\r'){
                          fwrite(&character, sizeof(character), 1, stdout );
                        }

                      }
                      
                    }
                    
                }
            }

        }
        // for (char i : line) {
        //     // //std::cout << i;
        //     fwrite(&i, sizeof(i), 1, stdout );
        // }
        c = '\n';
        fwrite(&c, sizeof(c), 1, stdout );
        // //std::cout<< line.size();
        // cout << endl;
        // fwrite( &line, sizeof(line), 1, stdout );
        // cout << &line;
        // line.clear();
        // for (const auto &i : characters) {
        //     cout << i << '-';
        // }
        // cout << endl;

        input_file.close();

        return EXIT_SUCCESS;
    }else{
        return EXIT_FAILURE;
    }
}
