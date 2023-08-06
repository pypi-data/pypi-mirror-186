# fkb: A knowledge base with file tracking and document note integration

Author: ArktisDev

Date: January 15, 2023

Derived from [kb](https://github.com/gnebbia/kb)

## Purpose

My ideal knowledge base should interface directly with the file hierarchy already on disk and allow me to add tags as well as longer notes to any digital object I choose. After searching for a long time I wasn't able to find a satifactory non-proprietary program that did this while also working on Linux, Mac, and Windows. Some programs even required using a GUI which wasn't going to work on a headless server for example. I eventually found [kb](https://github.com/gnebbia/kb) which has a great minimalist design and functions as a lightweight CLI but doesn't actually fulfill all my requirements.

Although kb does a great job of organizing notes it does not allow attaching notes to files which exist on the file hierarchy. For example I would be able to add a pdf file to KB but I would not be able to write a detailed note about the pdf file. Because of this I wrote fkb, a derivative of kb which allows adding files to the knowledge base and attaching notes to each file. As a result of this notes not attached to a file are not allowed in fkb while they are allowed in kb.

This sort of functionality is extremely useful for organizing all sorts of documents. Personally I use it to organize textbooks and academic papers as well as personal documents, cooking recipes, and images. Any sorts of documents can be organized using fkb.


## Installation

I use Python 3.9 but [vermin](https://github.com/netromdk/vermin) claims it should work with at least Python 3.6.

To install the most recent stable version just use pip:

```
pip install --user filekb
```

## Usage

After installing fkb for the first time it will prompt you to setup the directory to store fkb data as well as the root directory for your knowledge base. Files outside this root directory cannot be added to the knowledge base.

### Listing objects

List all objects using the `fkb list` command. It is optional to include additional filters on the objects. These are documented in the `fkb list --help` help menu.

Below you can see two quantum mechanics textbooks added to fkb.
![fkb_list_output](https://github.com/ArktisDev/fkb/blob/main/img/fkb_list.png?raw=true)

If you add a title to filter by only objects matching the filter are shown
![fkb_list_filter_output](https://github.com/ArktisDev/fkb/blob/main/img/fkb_list_filter.png?raw=true)

Specifying the `--verbose` option the file path on disk of the added objects is shown.
![fkb_list_file_path](https://github.com/ArktisDev/fkb/blob/main/img/fkb_list_file_path.png?raw=true)

### Adding objects
You can add objects to the database with `fkb add <path_to_object>`. Both absolute and relative paths work but the object must exist in your configured root directory. Additional options allow you to configure the author, category, and tags.

![fkb_add_object](https://github.com/ArktisDev/fkb/blob/main/img/fkb_add_object.png?raw=true)

### Updating objects
Once an object has been edited, it's title, category, author, tags can all be updated using the `fkb update` command. Since I didn't add a category to my solutions manual I added, let's do that now

![fkb_update_object](https://github.com/ArktisDev/fkb/blob/main/img/fkb_update_object.png?raw=true)


### Adding a note to an object
Given the id of an object `fkb note edit` can be used to edit a note for that object. This will open a text file in whichever editor you decided in the configuration of fkb. Once a note exists, it can be written to terminal using `fkb note cat`. In the example my note contains "This textbook covers...". The note can also be deleted completely with the `fkb note delete` command.

![fkb_note](https://github.com/ArktisDev/fkb/blob/main/img/fkb_note.png?raw=true)

### Searching through notes

Searching through notes can be done using the `fkb grep` command. In this example I added the text "a b c" to the GriffithQM object and "a b c d" to the GriffithQMSolutions object.

![fkb_grep](https://github.com/ArktisDev/fkb/blob/main/img/fkb_grep.png?raw=true)

### Backups

Backups of the knowledge base can be made with `fkb backup export`. The backup can then be imported using `fkb backup import`. It is not supported to import a backup using a different root knowledge base directory or fkb internal storage directory. This would be a good feature to implement however!

### Erasing knowledge base

The knowledge base can be erased using the `fkb erase` command. If you wish to keep configuration files but wipe only objects added to the knowledge base you can specify the option `fkb erase --db`.

### Watch for file changes

Because fkb keeps track of actual files on the disk, it should react to those files being renamed and moved by automatically updating the database entries for those files. The `fkb watch` command runs an infinite loop using the `watchdog` package to track file changes in the knowledge base root directory. I personally start `fkb watch` using a systemd user service that runs in the background, but there are at least 10 different ways to run `fkb watch` in the background automatically.

Below is an example of what `fkb watch` does running in the background. My changes to the file names are automatically propagated to the knowledge base.

![fkb_watch](https://github.com/ArktisDev/fkb/blob/main/img/fkb_watch.png?raw=true)

# Copyright

Copyright 2023, ArktisDev

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.