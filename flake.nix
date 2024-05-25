{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:

    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        python = pkgs.python312;
        llvmPackages = pkgs.llvmPackages_18;
        clang = llvmPackages.clang-unwrapped;
        cPackages = [ clang ];
        pythonPackages = [ python ];

        env = pkgs.mkShell {
          name = "devShell-${system}";
          buildInputs = pythonPackages ++ cPackages;

          shellHook = ''
            export PATH=${clang}/bin:$PATH
            export PYTHONPATH=${python}/lib/python3.12/site-packages:$PYTHONPATH
          '';
        };

      in {
        devShell = env;

        defaultPackage = env;
        apps.${system}.default = env;
      });
}
