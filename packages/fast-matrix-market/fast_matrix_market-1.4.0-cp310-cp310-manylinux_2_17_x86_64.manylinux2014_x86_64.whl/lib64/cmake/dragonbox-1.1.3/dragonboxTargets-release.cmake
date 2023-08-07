#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "dragonbox::dragonbox_to_chars" for configuration "Release"
set_property(TARGET dragonbox::dragonbox_to_chars APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(dragonbox::dragonbox_to_chars PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib64/libdragonbox_to_chars.a"
  )

list(APPEND _cmake_import_check_targets dragonbox::dragonbox_to_chars )
list(APPEND _cmake_import_check_files_for_dragonbox::dragonbox_to_chars "${_IMPORT_PREFIX}/lib64/libdragonbox_to_chars.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
