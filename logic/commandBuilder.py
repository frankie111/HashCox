from App import App


def build_command(app: App):
    hashcat_location = app.exec_selector_frame.exec_file_explorer.file_text_variable.get()
    hash_path = app.options_frame.hash_file_explorer.file_text_variable.get()
    hash_type = app.options_frame.hash_type
    device_type = app.options_frame.device_type_var.get()[0]
    workload_profile = app.options_frame.workload_profile_var.get()[0]
    disable_potfile = app.potfile_check_var.get()

    attack_mode = app.options_frame.attack_mode_frame.radio_var.get()

    hashcat_dir = hashcat_location.replace("hashcat.exe", "")
    potfile_text = "--potfile-disable" if int(disable_potfile) == 1 else ""
    base_command = f"cd {hashcat_dir} & hashcat.exe {hash_path} {potfile_text} -w {workload_profile} -D {device_type} -m {hash_type}" \
                   f" -a {attack_mode}"

    match attack_mode:
        case 0:
            return dictionary_attack(app, base_command)
        case 3:
            return bruteforce_attack(app, base_command)
        case _:
            print("Invalid attack mode")


def dictionary_attack(app: App, base_command):
    dictionary_file = app.options_frame.attack_mode_frame.dict_file_explorer.file_text_variable.get()
    command = base_command + f" {dictionary_file}"
    print(command)
    return command


def bruteforce_attack(app: App, base_command):
    option = app.options_frame.attack_mode_frame.brute_force_frame.radio_var.get()
    min_password_length = int(app.options_frame.attack_mode_frame.brute_force_frame.min_len_spinbox.spinbox.entry.get())
    max_password_length = int(app.options_frame.attack_mode_frame.brute_force_frame.max_len_spinbox.spinbox.entry.get())
    charset_entries = app.options_frame.attack_mode_frame.brute_force_frame.custom_charsets_frame.entries

    # Get the list of non-empty charsets
    charsets = list(map(lambda charset: charset.entry.get(), charset_entries))
    charsets = list(filter(lambda charset: charset != "", charsets))

    command = base_command
    match option:
        case 1:  # Lower Alpha
            command += f" {max_password_length * '?l'}"
        case 2:  # Upper Alpha
            command += f" {max_password_length * '?u'}"
        case 3:  # Numeric
            command += f" {max_password_length * '?d'}"
        case 4:  # Custom mask
            mask = app.options_frame.attack_mode_frame.brute_force_frame.mask_entry.get()

            # Define charsets in command
            for i in range(len(charsets)):
                command += f" -{i + 1} {charsets[i]}"

            command += f" {mask}"
        case _:
            pass

    command += f" -i --increment-min={min_password_length} --increment-max={max_password_length}"
    print(command)
    return command
