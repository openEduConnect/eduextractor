from eduextractor.sis.powerschool import PowerSchoolFrontend

if __name__ == '__main__':
    psf = PowerSchoolFrontend()
    psf.login()
    elem = psf._download_html_table('students.html')
