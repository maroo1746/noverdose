#include <stdio.h>
#include <mysql/mysql.h>

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


}

int main() {
    return 0;
}