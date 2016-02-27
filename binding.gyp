{
  "targets": [
    {
      "target_name": "node-sane",
      "sources": [
        "src/sane.cc",
        "src/sane_device.cc",
        "src/sane_handle.cc",
        "src/sane_option_descriptor.cc",
        "src/sane_parameters.cc"
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "/usr/local/include"
      ],
      "link_settings": {
        "libraries": [
          "-lsane", "-L/usr/local/lib"
        ]
      }
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
