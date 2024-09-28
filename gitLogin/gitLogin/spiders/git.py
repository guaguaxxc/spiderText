from gc import callbacks
from typing import Iterable
from xml.dom.minidom import parse

import scrapy
from scrapy import Request
#
# commit: Sign in
# authenticity_token: hvcH0Fl3obgI6n2pad8E7bDuEkKrG61GKi6Y2Mea5qPe/gd+je5RAaA5vFZcC3lMEUvrpMltKWlzwPVLdMoA0Q==
# add_account:
# login: guaguaxxc
# password: Cxx031105
# webauthn-conditional: undefined
# javascript-support: true
# webauthn-support: supported
# webauthn-iuvpaa-support: unsupported
# return_to: https://github.com/login
# allow_signup:
# client_id:
# integration:
# required_field_6476:
# timestamp: 1727523090530
# timestamp_secret: 7c80de8f45d2f7a06c7d58a351c0105655bc0db17156f092ab87a40b7ff6b2b5
# //*[@id="code-search-feedback-form"]/input[1]
# cookies的使用
class GitSpider(scrapy.Spider):
    name = "git"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/guaguaxxc"]

    def start_requests(self):
        url = self.start_urls[0]
        temp = '_octo=GH1.1.2114608641.1708158769; _device_id=1daee8912fe738dea33d11256a888094; MicrosoftApplicationsTelemetryDeviceId=031d0e81-8532-45ec-bda7-ade470cb275b; MSFPC=GUID=9378a325483c405194ad3fc3dbd8a50c&HASH=9378&LV=202402&V=4&LU=1708158899942; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; preferred_color_mode=light; tz=Asia%2FShanghai; saved_user_sessions=160313219%3AEfpG8boSx3ZwctjmWni0xxM58vkkV4Iot2C_5f6hsNUEI5mH; user_session=EfpG8boSx3ZwctjmWni0xxM58vkkV4Iot2C_5f6hsNUEI5mH; __Host-user_session_same_site=EfpG8boSx3ZwctjmWni0xxM58vkkV4Iot2C_5f6hsNUEI5mH; tz=Asia%2FShanghai; logged_in=yes; dotcom_user=guaguaxxc; _gh_sess=ktuaXxW9KWcbwGLipMqZv6E7kqJ4YJMg92TsS1FFFabdfqcbxgvw79%2BPsEATvRSeMqui%2FZmqmQ8G4qoGaUhM8x5BwlbRZQUONl9QE4KkUmjJUBf%2B7Qy6cjjAiC05lyEzcu58KpKloaRFAJTZR0Oh9XqZzbvmE3YB9m7fv35%2B5m0qAUvRKyZbCSQC5AO26hcB4n6ii82UCNJjX4mwMBaLy3O%2B95vXFqw54BRqU598DvhchDLNICq%2FmDIQz6EQrLnYjDGUNRfxEWNWm56IkYTufDFAjv7K9jV6yR%2BpUjk5%2FdSRqemiRGqGVWnvAfc0bOFXknIaVoTGYtSYco9o5tWSz9Kte9FrjGwIYQ9N5ZE%2FXBR55Z72cl7zOU8QNPEXqm%2BR5JkMxGwIQStQWl7Cj0mh8S8B%2Blthkzmtri9hYIjdyKRECgaNAoY25XqXVmWHpPA4TixY5BH%2FbK8IRaJIF0wQyZZ7ONI%2FnRV8iWaeIvBlvMac6FHgoVI4pbkkpSkQtVOuEqcc%2FWY53W3IRmZFd1yZtaf9JEqDFWjmQxSHt39KuPfSvT8uod3tXZ2E%2FiO2NXJYAJ%2FJNv9CU%2BHehPLKSIHWdAT3kB0giuAxFZYshGeXBHPikkAsSidSEwQ78EWszh76S%2BR07uOkkm7ifdP1jZ%2BW7D8qgYoLKBaZg7aadlZt1UPLRGFHrwPH%2BBJ%2F0FqJajAwEYjp2aX7rO3uWcew1tu8Ugy%2F499AmhwD8btWKcwM9jEQlBKJ0u0qIHVvOiO1A%2F0%2FxXl%2BoZEpJNT6mZg%2F%2FsaRJoDwsdKihMW9ZoMeyUAnQnS87aJchQEd8TTag9fYqsitxrspelC2wTypaEdY4E9SfHeb5WCHqLmZyZ0SiB2BktpkAi9LOqkLBQ%3D%3D--VcOZUf7DJ5jh4Z2N--2hPUuDuoeqhUpdVg1LztIw%3D%3D'
        cookies = {data.split('=')[0]: data.split('=')[-1] for data in temp.split(';')}
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response, **kwargs):
        print(response.xpath('/html/head/title/text()').extract_first())
