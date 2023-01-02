# Libraries (Google API Client and colorama)
from googleapiclient.discovery import build
from colorama import Fore, Back, Style, init
init(autoreset=True)

# Credential required to use "Custom Search API"
API_KEY = ""  # --> INSERT YOUR OWN API KEY
# Search engine ID
CX = ""  # --> INSERT YOUR OWN SEARCH ENGINE ID

# Name and version of the service (Custom Search API v1)
resource = build('customsearch', 'v1', developerKey=API_KEY).cse()


def showOptions():
    showHeader()
    print("\n")
    print("  1.  Subdomains")
    print("  2.  Directory Listing")
    print("  3.  Login and registration pages")
    print("  4.  Files")
    print("  5.  Keywords")
    print("  6.  Default pages")
    print("  7.  Software versions")
    print("  8.  Error messages")
    print("  9.  Databases")
    print("  10. Email addresses and phone numbers")
    print("  11. Employees")

    showInput1()


def showHeader():
    print("\n")
    print(Fore.YELLOW + Style.BRIGHT +
          "  |*|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|*|")
    print(Fore.YELLOW + Style.BRIGHT +
          "  |                                                                                                |")
    print(Fore.YELLOW + Style.BRIGHT +
          "  |                                   GoogleHackingByDomain v1.0                                   |")
    print(Fore.YELLOW + Style.BRIGHT +
          "  |                                       By Juan Tomás Ortiz                                      |")
    print(Fore.YELLOW + Style.BRIGHT +
          "  |                                 *For legitimate purposes only*                                 |")
    print(Fore.YELLOW + Style.BRIGHT +
          "  |                                                                                                |")
    print(Fore.YELLOW + Style.BRIGHT +
          "  |*|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|=||=|=|*|")


def showInput1():
    print("\n  =================================================================================================")
    print(Fore.CYAN + Style.BRIGHT + "  Type a domain name: ", end='')
    domain = input()
    print(Fore.CYAN + Style.BRIGHT + "  Type an option: ", end='')
    option = int(input())
    print("  =================================================================================================")
    try:
        search(domain, option)
        showInput2()
    except:
        print(Fore.RED + Style.BRIGHT +
              "\n  Error occurred. Please try again. \n")


def showInput2():
    print(Style.RESET_ALL + " ")
    result = input("  Do you want to try another option? (Y/N): ").lower()
    if result == "y":
        showOptions()


def search(domain, option):
    if option == 1:
        resultsQueries = []
        results = []
        format = 'link'
        site = 'site:' + domain

        print("  Searching for subdomains for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute query for subdomains (page 1 and 2)
        resultsQueries.append(resource.list(
            q=site + ' -inurl:www.' + domain, cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' -inurl:www.' + domain, cx=CX, start=11).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Subdomains", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for subdomains.")

    elif option == 2:
        resultsQueries = []
        results = []
        format = 'titleAndLink'
        site = 'site:' + domain

        print("  Searching for directory listing for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute query for directory listing (page 1 and 2)
        resultsQueries.append(resource.list(
            q=site + ' intitle:"Index of"', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' intitle:"Index of"', cx=CX, start=11).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Directory Listing", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for directory listing.")

    elif option == 3:
        resultsQueries = []
        results = []
        format = 'titleAndLink'
        site = 'site:' + domain

        print(
            "  Searching for login and registration pages for the domain " +
            Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for login pages (3)
        resultsQueries.append(resource.list(
            q=site + ' (Login | "Sign in" | Signin | Portal)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ("Iniciar sesion" | "Inicia sesion" | Cuenta)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Acceso | Acceder | Ingreso | Ingresar)', cx=CX).execute())

        # Execute queries for register pages (3)
        resultsQueries.append(resource.list(
            q=site + ' (Register | Registration | "Create account" | "Create your account")', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ("Sign up" | Signup)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Registrate | Registrarse | "Crea tu cuenta" | "Crear cuenta" | "Alta de usuario")', cx=CX).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(
                results, "Login and registration pages", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for login and registration pages.")

    elif option == 4:
        resultsQueries = []
        results = []
        format = 'titleAndLink'
        site = 'site:' + domain

        print("  Searching for file types for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for file types (15)
        resultsQueries.append(resource.list(
            q=site + ' ext:pdf', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:pdf', cx=CX, start=11).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:xls', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:txt', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:xml', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:doc', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:docx', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:ini', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:config', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:conf', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:cfg', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:log', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:sql', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:bak', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ext:php', cx=CX).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Files", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for file types.")

    elif option == 5:
        resultsQueries = []
        results = []
        format = 'all'
        site = 'site:' + domain

        print("  Searching for keywords for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for keywords (15)
        resultsQueries.append(resource.list(
            q=site + ' (Password | Passwords)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Contraseña | Contraseñas)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Clave | Claves)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (User | Username | Users)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Usuario | "Nombre de usuario" | Usuarios)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Cuenta | Cuentas)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Account | Accounts)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Admin | Administrador | Administrativo)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Administrator | Administrators | Administrative)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Confidencial | Sensible | Confidential | Sensitive)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Privado | Private)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Files | Backup | Backups)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Wordpress | wp)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Intranet | Interno | Internal)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (API | Key | GitHub)', cx=CX).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Keywords", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT + "\n  No results found for keywords.")

    elif option == 6:
        resultsQueries = []
        results = []
        format = 'all'
        site = 'site:' + domain

        print("  Searching for default pages for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for default pages (7)
        resultsQueries.append(resource.list(
            q=site + ' ("Welcome to" | "Bienvenido a")', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ("Por defecto" | Default)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Instalacion | Installation)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Documentacion | Documentation | Manual)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Prueba | "Test page")', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Config | Configuracion | Configuration)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Wordpress | wp)', cx=CX).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Default pages", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for default pages.")

    elif option == 7:
        resultsQueries = []
        results = []
        format = 'all'
        site = 'site:' + domain

        print("  Searching for software versions for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for software versions (6)
        resultsQueries.append(resource.list(
            q=site + ' Apache', cx=CX).execute())
        resultsQueries.append(resource.list(q=site + ' PHP', cx=CX).execute())
        resultsQueries.append(resource.list(q=site + ' IIS', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' "Server at"', cx=CX).execute())
        resultsQueries.append(resource.list(q=site + ' Port', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Windows | Win32 | Unix | Linux | Debian | Ubuntu | RedHat)', cx=CX).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Software versions", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for software versions.")

    elif option == 8:
        resultsQueries = []
        results = []
        format = 'all'
        site = 'site:' + domain

        print("  Searching for error messages for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for error messages (6)
        resultsQueries.append(resource.list(
            q=site + ' (Syntax | Error)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Fatal | Incorrect | Bad | Exception)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ("Not found" | Forbidden | "Bad request" | Unauthorized | "Internal Server Error")', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Request | Internal)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Unavailable | Unable)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (400 | 401 | 403 | 404 | 500)', cx=CX).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Error messages", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for error messages.")

    elif option == 9:
        resultsQueries = []
        results = []
        format = 'all'
        site = 'site:' + domain

        print("  Searching for databases for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for databases (8)
        resultsQueries.append(resource.list(
            q=site + ' (Database | Databases | "Base de datos" | basededatos | db | bd)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Tabla | Table | Filas | Columnas | Rows | Columns | Data)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ("Running on" | SQL | MySQL)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Query | Queries | Consulta | Consultas)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (phpMyAdmin | phpPgAdmin)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Connect | Connection | Conexion)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Dumping | Dump)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' ("Insert into" | "Create table")', cx=CX).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Databases", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for databases.")

    elif option == 10:
        resultsQueries = []
        results = []
        format = 'description'
        companyName = getCompanyName(domain)
        site = 'site:' + domain

        print("  Searching for email addresses and phone numbers for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for email addresses and phone numbers (5)
        resultsQueries.append(resource.list(
            q=site + ' (Correo | Email | Mail)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Numero | Telefono | Contacto)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (Phone | Number | Contact)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=site + ' (+54 | +57 | +56 | +598 | +595 | +51 | +58 | +55 | +593 | +52 | +1)', cx=CX).execute())
        resultsQueries.append(resource.list(
            q=('intext:' + domain + ' -intext:www -intext:https'), cx=CX).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(
                results, "Email addresses and phone numbers", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for email addresses and phone numbers.")

    elif option == 11:
        resultsQueries = []
        results = []
        format = 'titleAndLink'
        companyName = getCompanyName(domain)

        print("  Searching for employees for the domain " +
              Fore.GREEN + Style.BRIGHT + domain)

        # Execute queries for employees (page 1 and 2)
        resultsQueries.append(resource.list(
            q='site:linkedin.com/in intitle:' + companyName, cx=CX).execute())
        resultsQueries.append(resource.list(
            q='site:linkedin.com/in intitle:' + companyName, cx=CX, start=11).execute())

        # Get the results
        results = getResults(resultsQueries)

        # Show the results and generate the output file
        if (len(results) > 0):
            showResults(results, format)
            createResultsFile(results, "Employees", domain, format)
        else:
            print(Fore.RED + Style.BRIGHT +
                  "\n  No results found for employees.")

    else:
        print(Fore.RED + Style.BRIGHT + "\n  Invalid option, please try again.")
        showInput1()

# Different formats on how the results are displayed


def showResults(results, format):
    print("  =================================================================================================")
    print("\n")
    print("  " + Back.BLACK + Fore.GREEN +
          Style.DIM + "Results showed:", len(results))
    print("  =================================================================================================")
    if (format == 'link'):
        for item in results:
            print(Fore.GREEN + "  " + item['displayLink'])
    elif (format == 'description'):
        for item in results:
            if ('snippet' in item):
                print(Fore.YELLOW + Style.BRIGHT +
                      "  Description: " + item['snippet'])
                print(" ")
    elif (format == 'titleAndLink'):
        for item in results:
            print(Fore.MAGENTA + Style.BRIGHT + "  " + item['title'])
            print(Fore.GREEN + "  " + item['link'])
            print(" ")
    elif (format == 'all'):
        for item in results:
            print(Fore.MAGENTA + Style.BRIGHT + "  " + item['title'])
            print(Fore.GREEN + "  " + item['link'])
            if ('snippet' in item):
                print(Fore.YELLOW + Style.BRIGHT + "  " + item['snippet'])
            print(" ")
    print("  =================================================================================================")


def getResults(resultsQueries):
    results = []
    for resultQuery in resultsQueries:
        if (int(resultQuery['searchInformation']['totalResults']) > 0):
            results += resultQuery['items']
    return results


def getCompanyName(domain):
    companyName = ''
    for char in domain:
        if char == '.':
            break
        else:
            companyName += char
    return companyName


def createResultsFile(results, title, domain, format):
    with open(title + ' - ' + domain + ' - GoogleHackingByDomain.txt', 'w') as f:
        f.write('GoogleHackingByDomain: ' + title + ' - ' + domain + '\n')
        f.write('================================================================================================= \n \n')
        if (format == 'link'):
            for item in results:
                f.write(item['displayLink'])
                f.write('\n')
        elif (format == 'description'):
            for item in results:
                if ('snippet' in item):
                    f.write("Description: " + item['snippet'])
                    f.write('\n \n')
        elif (format == 'titleAndLink'):
            for item in results:
                f.write(item['title'])
                f.write('\n')
                f.write(item['link'])
                f.write('\n \n')
        elif (format == 'all'):
            for item in results:
                f.write(item['title'])
                f.write('\n')
                f.write(item['link'])
                f.write('\n')
                if ('snippet' in item):
                    f.write(item['snippet'])
                f.write('\n \n')
        f.write('=================================================================================================')
        f.close()


showOptions()
