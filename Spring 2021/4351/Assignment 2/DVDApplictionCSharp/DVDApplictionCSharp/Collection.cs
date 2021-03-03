using System;
using System.Collections.Generic;
using System.Text;

namespace DVDApplictionCSharp
{
    public class Collection
    {
        private DVD[] dvd
        {
            get => default;
            set
            {
            }
        }

        private int MAX_NUM_DVDS
        {
            get => default;
            set
            {
            }
        }

        private int numOfDVDs
        {
            get => default;
            set
            {
            }
        }

        public void addDVD(string category, float price, string time, string title, int year)
        {
            throw new System.NotImplementedException();
        }

        public void removeDVD(string title)
        {
            throw new System.NotImplementedException();
        }

        public void editDVD(string category, float price, string time, string title, int year)
        {
            throw new System.NotImplementedException();
        }

        public void displayByCat()
        {
            throw new System.NotImplementedException();
        }

        public void displayByYear()
        {
            throw new System.NotImplementedException();
        }

        public void restoreCollection()
        {
            throw new System.NotImplementedException();
        }

        public void saveCollection()
        {
            throw new System.NotImplementedException();
        }
    }
}