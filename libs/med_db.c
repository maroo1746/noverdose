#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <mysql/mysql.h>

void write_to_log(const char* message) {

    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        fprintf(stderr, "Current working dir: %s\n", cwd);
    } else {
        perror("getcwd() error");
    }

    const char* log_file = "log.txt";
    FILE* fp = fopen(log_file, "a");

    if (!fp) {
        fprintf(stderr, "Failed to open log file\n");
        return;
    }

    fprintf(fp, "%s\n", message);
    fclose(fp);
}

void insert_into_med_db(const char* product_name, const char* compound_name, const char* compound_code, const char* product_code, const char* company_name) {
    MYSQL *con = mysql_init(NULL);

    if (con == NULL) {
        fprintf(stderr, "mysql_init() failed\n");
        return;
    } 

    if(mysql_real_connect(con, "db", "root", "snewi832#", "med_db", 3306, NULL, 0) == NULL) {
        fprintf(stderr, "%s\n", mysql_error(con));
        mysql_close(con);
        return;
    }
    
    char query[500];
    sprintf(query, "INSERT INTO med(product_name, compound_name, compound_code, product_code, company_name) VALUES('%s', '%s', '%s', '%s', '%s')", product_name, compound_name, compound_code, product_code, company_name);

    if (mysql_query(con, query)) {
        fprintf(stderr, "%s\n", mysql_error(con));
        mysql_close(con);
        return;
    }

    printf(stderr, product_name); 
    printf(stderr, " inserted into med table successfully\n");

    char log_message[600];
    sprintf(log_message, "Inserted: %s, %s, %s, %s, %s", product_name, compound_name, compound_code, product_code, company_name);
    write_to_log(log_message); 

    mysql_close(con);

}

int main() {
    return 0;
}