# global variables
memory = ["000" for i in range(100)]
# -- registers --
program_counter = 0
accumulator = 0
memory_address_register = 0
memory_data_register = "00"
current_instruction_register = "00"

def load_program_to_memory(instruction_list):
    # error-handling: instruction count cannot exceed number of memory addresses
    for i in range(len(instruction_list)):
        memory[i] = instruction_list[i]

def fetch_instruction(instruction_address):
    return memory[instruction_address]

def decode_instruction(instruction):
    instruction_set = { "901" : "input",
                        "902" : "output",
                        "000" : "halt"
                      }
    current_instruction = instruction_set[instruction]
    return current_instruction

def execute_instruction():
    pass

def main():
    program = ["901", "902", "000"]
    load_program_to_memory(program)
    
    # fetch
    memory_address_register = program_counter
    memory_data_register = fetch_instruction(memory_address_register)
    current_instruction_register = memory_data_register
    # decode
    decode_instruction(current_instruction_register)
    # execute

if __name__ == "__main__":
    main()