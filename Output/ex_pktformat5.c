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

#include ex_pktformat5.h

int preapre_packet(void *buf, int *len, pktformat5 *arg_pktformat5)
{
	if(buf == NULL || len == NULL)
		return -1;

	memcpy((char*)buf, (char*)arg_pktformat5, sizeof(pktformat5));
	
	*len = sizeof(pktformat5);
	return 0;
}
	 
int parse_packet(void *buf, int *len, pktformat5 *arg_pktformat5)
{
	if(buf == NULL || len == NULL)
		return -1;

	if(*len != sizeof(pktformat5)
		return -1;

	memcpy((char*)arg_pktformat5, (char*)buf, sizeof(pktformat5));
	
	return 0;
}

void print_packet(pktformat5 *arg_pktformat5)
{
	printf("Value of FIELD1 : %d \n", arg_pktformat5->field1);
	printf("Value of FIELD2 : %d \n", arg_pktformat5->field2);
	printf("Value of FIELD3 : %d \n", arg_pktformat5->field3);
	printf("Value of FIELD5 : %d \n", arg_pktformat5->field5);
	printf("Value of FIELD6 : %d \n", arg_pktformat5->field6);

}
