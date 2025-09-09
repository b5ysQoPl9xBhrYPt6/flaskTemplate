import project

def main():
    project.loadenv.migrate()
    project.project.run()

if __name__ == '__main__':  main()