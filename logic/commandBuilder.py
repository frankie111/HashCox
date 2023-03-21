from App import App


def build_command(app: App):
    hashcat_location = app.exec_selector_frame.exec_file_explorer.file_text_variable.get()
    hash_path = app.options_frame.hash_file_explorer.file_text_variable.get()
    hash_type = app.options_frame.hash_type
    device_type = app.options_frame.device_type_var.get()[0]
    workload_profile = app.options_frame.workload_profile_var.get()[0]

    attack_mode = app.options_frame.attack_mode_frame.radio_var.get()

    match attack_mode:
        case 0:
            return dictionary_attack(app, attack_mode, hashcat_location, hash_path, hash_type, device_type,
                                     workload_profile)
        case 3:
            return bruteforce_attack(app)
        case _:
            print("Invalid attack mode")


def dictionary_attack(app: App, attack_mode, hashcat_location, hash_path, hash_type, device_type, workload_profile):
    dictionary_file = app.options_frame.attack_mode_frame.dict_file_explorer.file_text_variable.get()
    command = f"cd D:\\kit\\hashcat\\ & {hashcat_location} -w {workload_profile} -D {device_type} -m {hash_type} -a {attack_mode} {hash_path}" \
              f" {dictionary_file}"
    print(command)
    return command


def bruteforce_attack(app: App):
    pass
