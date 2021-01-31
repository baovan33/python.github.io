import scan_url
import save_url

def main():
    url = input('Nhập link ban đầu: ')
    page_max = int(input('nhập số lượng trang: '))
    url = scan_url.sua_url(url)
    waiting_line = scan_url.search_url(url, url)
    history = scan_url.add_link(waiting_line, url, page_max)

    save_url.make_dir(input('Nhập tên thư mục lưu file: '))
    save_url.save_all(history, page_max)

if __name__ == '__main__':
    main()