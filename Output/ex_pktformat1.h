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

#ifndef EX_PKTFORMAT1_H_
#define EX_PKTFORMAT1_H_

typedef struct __atribute__((packed)) pktformat1
{
	int field1;
	char field2;
	int field3;
	long field4;
};


#endif //EX_PKTFORMAT1_H_
