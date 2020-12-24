import sys
import tabula

def main():
    # ------------------------------------------------------------------
    sys.stderr.write("*** 開始 ***\n")
    #
    # file_pdf = sys.argv[1]
    # file_csv = sys.argv[2]

    # tabula.convert_into(file_pdf, file_csv, pages="all", output_format="csv")
    tabula.convert_into('list_all.pdf', 'out.csv', pages="all", output_format="csv")
    #
    sys.stderr.write("*** 終了 ***\n")

if __name__ == "__main__":
    main()