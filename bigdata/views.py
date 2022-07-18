from django.shortcuts import render
import pandas as pd
from django.core.files.storage import FileSystemStorage
from .models import Life_Expectancy
from django.contrib import messages


# Create your views here.
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('myfile'):
        #uploading exel
        file = request.FILES['myfile']        
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url
        print(excel_file)
        response_data = {}
        response_data['ok'] = "Uploaded successful"

        #read csv file
        df = pd.read_csv("."+excel_file,encoding='utf-8')


    
        #create titles from the row indexed 1
        header_row = 1
        df.columns = df.iloc[header_row]

        #remove first row which is unwanted
        df = df.drop([0])

        #convert dataset from  wide to long
        df = pd.melt(df, id_vars=['Country Name', 'Country Code'], value_vars=[i for i in range(1990, 1991)], value_name='Age')

        #rename columns names
        df.rename(columns = {'Country Name':'country_name', 'Country Code':'country_code' ,1:'Year'}, inplace = True)

        # print(df.columns)
        df = df.itertuples()
        for data in df:
            # print(f'{data.country_name} {data.country_code} {data.Age} {data.Year} ')
            obj = Life_Expectancy.objects.create(
                country_name =data.country_name,country_code=data.country_code, year=data.Year, age=data.Age)
            obj.save()
            messages.success(request, 'File Exported Successful scroll down/search to see all data')


    data = Life_Expectancy.objects.all()
    year_filter = Life_Expectancy.objects.filter(country_name ='Tanzania')
    country_filter = Life_Expectancy.objects.filter(year ='1990.0')
    context = {
        'data':data,
        'year_filter':year_filter,
        'country_filter':country_filter
    }

    return render(request, 'table.html', context)



def graph(request, name):
    labels = []
    data = []
    edata =  Life_Expectancy.objects.filter(country_name=name)
    for mydata in edata:
        labels.append(mydata.year)
        data.append(mydata.age)
    context = {
        'labels':labels,
        'data':data,
        'edata':edata[:1]
    }
    return render(request, 'graph.html', context)