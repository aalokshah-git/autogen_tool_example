/***************************************************
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
* 
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
* 
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <https://www.gnu.org/licenses/>.
* 
* Author : Aalok Shah
* Version : 0.0.1
*******************************************************/

#include ex_pktformat3.h

int preapre_packet(void *buf, int *len, pktformat3 *arg_pktformat3)
{
	if(buf == NULL || len == NULL)
		return -1;

	memcpy((char*)buf, (char*)arg_pktformat3, sizeof(pktformat3));
	
	*len = sizeof(pktformat3);
	return 0;
}
	 
int parse_packet(void *buf, int *len, pktformat3 *arg_pktformat3)
{
	if(buf == NULL || len == NULL)
		return -1;

	if(*len != sizeof(pktformat3)
		return -1;

	memcpy((char*)arg_pktformat3, (char*)buf, sizeof(pktformat3));
	
	return 0;
}

void print_packet(pktformat3 *arg_pktformat3)
{
	printf("Value of FIELD1 : %c \n", arg_pktformat3->field1);
	printf("Value of FIELD2 : %c \n", arg_pktformat3->field2);
	printf("Value of FIELD3 : %d \n", arg_pktformat3->field3);
	printf("Value of FIELD1 : %f \n", arg_pktformat3->field1);
	printf("Value of FIELD2 : %d \n", arg_pktformat3->field2);
	printf("Value of FIELD3 : %c \n", arg_pktformat3->field3);
	printf("Value of FIELD4 : %f \n", arg_pktformat3->field4);
	printf("Value of FIELD5 : %d \n", arg_pktformat3->field5);
	printf("Value of FIELD6 : %c \n", arg_pktformat3->field6);
	printf("Value of FIELD7 : %d \n", arg_pktformat3->field7);
	printf("Value of FIELD8 : %c \n", arg_pktformat3->field8);

}
