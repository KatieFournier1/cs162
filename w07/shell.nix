let
  nixpkgs = import <nixpkgs> {};
in nixpkgs.mkShell {
  packages = [
    (nixpkgs.python313Full.withPackages (pypkgs: with pypkgs; [
    ]))
  ];
  shellHook = "fish; exit";
}
