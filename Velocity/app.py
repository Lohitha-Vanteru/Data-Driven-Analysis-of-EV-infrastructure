from flask import Flask, session, abort, redirect, request, render_template
import boto3
import csv
import json
import folium
import pgeocode
import pandas as pd
import io

app = Flask("evcharge")  #naming our application
app.config["TEMPLATES_AUTO_RELOAD"] = True

zipCode = '95133'
vehicleType = ''

@app.route("/")
def index():
	global vehicleType
	vehicleType = ""
	return render_template('index.html')

#home page 
@app.route("/home")
def home():
    global vehicleType
    global zipCode
    zipCode = "95133"
    vehicleType = ""
    return render_template('home.html')

@app.route("/countywise")
def countyWiseEVs():
	county = request.args.get('county', default = 'Alameda', type = str)
	year = request.args.get('year', default = '2023', type = str)

	s3_client = boto3.client('s3',
		aws_access_key_id="<AWS_ACCESS_KEY>",
		aws_secret_access_key="<AWS_SECRET_KEY>"
	)

	response = s3_client.get_object(Bucket="data298b-t6-results-data", Key="Countywise_evcs_count_data.csv")
	lines = response['Body'].read().decode('utf-8').splitlines(True)
	reader = csv.DictReader(lines)
	result = {}
	for row in reader:
		# csv_header_key is the header keys which you have defined in your csv header
		if(row['County'] == county and row['Year'] == year):
			result = json.dumps(row, indent = 4)
			break			
	return result

@app.route("/zipcodewise")
def zipCodeWiseEVs():
	zipCodeInput = request.args.get('zipCode', default = '95192', type = str)
	year = request.args.get('year', default = '2023', type = str)

	s3_client = boto3.client('s3',
		aws_access_key_id="<AWS_ACCESS_KEY>",
		aws_secret_access_key="<AWS_SECRET_KEY>"
	)

	response = s3_client.get_object(Bucket="data298b-t6-results-data", Key="Zipcodewise_evcs_count_data_.csv")
	lines = response['Body'].read().decode('utf-8').splitlines(True)
	reader = csv.DictReader(lines)
	result = {}
	for row in reader:
		if(row['ZIP'] == zipCodeInput and row['Year'] == year):
			result = json.dumps(row, indent = 4)
			break			
	return result

@app.route("/updatezipcode")
def updateZipCode():
	global zipCode
	global vehicleType
	vehicleType = ''
	zipCode = request.args.get('zipCode', default = '95133', type = str)
	return {'zipCode': zipCode}

@app.route("/updatevehicletype")
def updateVehicleType():
	global vehicleType
	vehicleType = request.args.get('vehicleType', default = '', type = str)
	return {'vehicleType': vehicleType}

@app.route("/map")
def map():
	global zipCode
	global vehicleType

	nomi = pgeocode.Nominatim('us')
	query = nomi.query_postal_code(zipCode)
	map = folium.Map(location=[query["latitude"], query["longitude"]], zoom_start=12)

	s3_client = boto3.client('s3',
		aws_access_key_id="<AWS_ACCESS_KEY>",
		aws_secret_access_key="<AWS_SECRET_KEY>"
	)
	existingChargingStations = s3_client.get_object(Bucket="data298b-t6-results-data", Key="Existing_Charging_Stations.csv")
	ecs_lines = existingChargingStations['Body'].read().decode('utf-8').splitlines(True)
	ecs_reader = csv.DictReader(ecs_lines)

	zipCodeWiseEVs = s3_client.get_object(Bucket="data298b-t6-results-data", Key="Zipcodewise_evcs_count_data_.csv")

	zcw_df = pd.read_csv(io.BytesIO(zipCodeWiseEVs['Body'].read()))
	projEV2024 = zcw_df[(zcw_df['ZIP'] == int(zipCode)) & (zcw_df['Year'] == 2024)]
	projEV2025 = zcw_df[(zcw_df['ZIP'] == int(zipCode)) & (zcw_df['Year'] == 2025)]
	projEV2026 = zcw_df[(zcw_df['ZIP'] == int(zipCode)) & (zcw_df['Year'] == 2026)]
	
	for row in ecs_reader:
		if(row['ZIP'] == zipCode):
			tooltipHtml = f"""
				<table style="font-size: 18px;">
					<tr><td>Station Name:</td><td>{row['Station Name']}</td></tr>
					<tr><td>Address:</td><td>{row['Street Address']}</td></tr>
					<tr><td>City:</td><td>{row['City']}</td></tr>
					<tr><td># Level 2 Chargers:</td><td>{row['EV Level2 EVSE Num']}</td></tr>
					<tr><td># Fast Chargers:</td><td>{row['EV DC Fast Count'] or 0}</td></tr>
					<tr><td>EV Connector Types:</td><td>{row['EV Connector Types']}</td></tr>
					<tr><td># Projected EV Stations - 2024:</td><td>{int(projEV2024['EV_Level2_EVSE_Num'].item() + projEV2024['EV_DC_Fast_Count'].item())}</td></tr>
					<tr><td># Projected EV Stations - 2025:</td><td>{int(projEV2025['EV_Level2_EVSE_Num'].item() + projEV2025['EV_DC_Fast_Count'].item())}</td></tr>
					<tr><td># Projected EV Stations - 2026:</td><td>{int(projEV2026['EV_Level2_EVSE_Num'].item() + projEV2026['EV_DC_Fast_Count'].item())}</td></tr>
				</table>
			"""
			folium.Marker(
		      	location=[row['Latitude'], row['Longitude']],
		      	tooltip = tooltipHtml,
		      	icon=folium.Icon(color='green', icon='plug', prefix='fa')
		   	).add_to(map)

	if vehicleType == "SchoolBus" or vehicleType == "All":
		schoolBusStations = s3_client.get_object(Bucket="data298b-t6-results-data", Key="California_Schools_2022-23.csv")
		sbs_df = pd.read_csv(io.BytesIO(schoolBusStations['Body'].read()))
		sbs_df = sbs_df[sbs_df['Zip'] == float(zipCode)]
		sbs_df = sbs_df.sample(frac =.3)

		for index, row in sbs_df.iterrows():
			tooltipHtml = f"""
				<table style="font-size: 18px;">
					<tr><td>Station Name:</td><td>{row['SchoolName']}</td></tr>
					<tr><td>Address:</td><td>{row['Street']}</td></tr>
					<tr><td>City:</td><td>{row['City']}</td></tr>
				</table>
			"""
			folium.Marker(
		      	location=[row['Latitude'], row['Longitude']],
		      	tooltip = tooltipHtml,
		      	icon=folium.Icon(color='orange', icon='bus', prefix='fa')
		   	).add_to(map)

	if vehicleType == "TransitBus" or vehicleType == "All":
		transitBusStations = s3_client.get_object(Bucket="data298b-t6-results-data", Key="bus_stop_zc.csv")
		tbs_df = pd.read_csv(io.BytesIO(transitBusStations['Body'].read()))
		tbs_df = tbs_df[tbs_df['Zip'] == float(zipCode)]

		for index, row in tbs_df.iterrows():
			tooltipHtml = f"""
				<table>
					<tr><td>Station Name:</td><td>{row['name']}</td></tr>
				</table>
			"""
			folium.Marker(
		      	location=[row['Latitude'], row['Longitude']],
		      	tooltip = tooltipHtml,
		      	icon=folium.Icon(color='blue', icon='bus', prefix='fa')
		   	).add_to(map)

	if vehicleType == "DeliveryTruck" or vehicleType == "All":
		deliveryTruckStations = s3_client.get_object(Bucket="data298b-t6-results-data", Key="Deliverytruck_evcs.csv")
		dts_df = pd.read_csv(io.BytesIO(deliveryTruckStations['Body'].read()))
		dts_df = dts_df[dts_df['ZIP'] == float(zipCode)]

		for index, row in dts_df.iterrows():
			tooltipHtml = f"""
				<table>
					<tr><td>Address:</td><td>{row['Address']}</td></tr>
				</table>
			"""
			folium.Marker(
		      	location=[row['Latitude'], row['Longitude']],
		      	tooltip = tooltipHtml,
		      	icon=folium.Icon(color='purple', icon='truck', prefix='fa')
		   	).add_to(map)

	iframe = map.get_root()._repr_html_()
	return iframe

