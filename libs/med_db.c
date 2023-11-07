#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <mysql/mysql.h>

#define LOG_FILE "log.txt"
#define LOG_FILE_MODE S_IRUSR | S_IWUSR

void write_to_log(const char* message) {
    int fd = open(LOG_FILE, O_WRONLY | O_CREAT | O_APPEND, LOG_FILE_MODE);
    if (fd == -1) {
        perror("Failed to open log file");
        return;
    }

    // fd를 FILE*로 변환합니다.
    FILE* fp = fdopen(fd, "a");
    if (!fp) {
        perror("Failed to convert file descriptor to file pointer");
        close(fd);
        return;
    }

    fprintf(fp, "%s\n", message);
    fclose(fp); // fclose는 내부적으로 fd도 닫습니다.
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

    fprintf(stderr, product_name); 
    fprintf(stderr, " inserted into med table successfully\n");

    char log_message[600];
    snprintf(log_message, sizeof(log_message), "Inserted: %s, %s, %s, %s, %s", product_name, compound_name, compound_code, product_code, company_name);
    write_to_log(log_message); 

    mysql_close(con);

}

int main() {
    return 0;
}