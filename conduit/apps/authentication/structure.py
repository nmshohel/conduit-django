Model: PBSInfo
    Fields: 
    management_id,
    pbs_code, 001
    pbs_name_en,
    pbs_name_bn,
    address_en,
    address_bn,
    lat_long_value,
    office_head_name,
    office_head_Designation,
    office_head_mobile_num,
    complain_center_mobile_num,
    pbs_logo,
    total_consumer_nos,
    total_billing_consumer_nos,
    total_service_area_km,
    total_line_km,
    total_employee_nos


Model: MainOfficeInfo
    Fields:
    pbs_code, 001
    office_code,
    office_category
    office_type 
    office_name_en,
    office_name_bn,
    office_address_en,
    office_address_bn,
    lat_long_value,
    office_head_name,
    office_head_Designation,
    office_head_mobile_num,
    complain_center_mobile_num,
    total_consumer_nos,
    total_billing_consumer_nos,
    total_service_area_km,
    total_line_km,
    total_employee_nos 

Model: SubOfficeInfo
    Fields:
    pbs_code, 001
    main_office_code,
    office_category
    office_type,
    suboffice_code,
    suboffice_name_en,
    suboffice_name_bn,
    suboffice_address_en,
    suboffice_address_bn,
    lat_long_value,
    office_head_name,
    office_head_Designation,
    office_head_mobile_num,
    complain_center_mobile_num,
    total_consumer_nos,
    total_billing_consumer_nos,
    total_service_area_km,
    total_line_km,
    total_employee_nos


Model: OfficeType
    Fields: 
    type_code, 062
    name_en,0620
    name_bn,
    office_category

Model: ManagementInfo
    Fields:
    management_id,
    management_name