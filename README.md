- [Setup](#2db4af5d-6f9c-4ea2-bec0-4dc571176e4d)


<a id="2db4af5d-6f9c-4ea2-bec0-4dc571176e4d"></a>

# Setup

-   [Poetry](https://poetry.eustace.io/) is used to manage the project. You will need to install it if you have not already.

    ```sh
    pip3 install --user poetry
    ```

-   Clone [this repository](https://github.com/jumipeca/Ahorro_Combustible)

    ```sh
    git clone https://github.com/jumipeca/Ahorro_Combustible.git
    ```

-   [Update](https://poetry.eustace.io/docs/cli/#update) the dependencies.

    ```sh
    poetry update
    ```

    This command will create a virtual environment and download packages for your project as shown below.

        Creating virtualenv ahorro-combustible-py3.7 in ~/.cache/pypoetry/virtualenvs
        Updating dependencies
        Resolving dependencies... (3.5s)

        Writing lock file


        Package operations: 14 installs, 0 updates, 0 removals

          - Installing more-itertools (7.2.0)
          - Installing zipp (0.6.0)
          - Installing attrs (19.1.0)
          - Installing importlib-metadata (0.19)
          - Installing pyparsing (2.4.2)
          - Installing six (1.12.0)
          - Installing atomicwrites (1.3.0)
          - Installing packaging (19.1)
          - Installing pluggy (0.12.0)
          - Installing py (1.8.0)
          - Installing wcwidth (0.1.7)
          - Installing coverage (4.5.4)
          - Installing pytest (5.1.1)
          - Installing pytest-cov (2.7.1)

-   To activate your virtual environment move to your project folder and run [poetry shell](https://poetry.eustace.io/docs/cli/#shell).
