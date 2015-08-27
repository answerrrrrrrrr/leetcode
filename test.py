import traceback

class test_t():
    def __init__(self, num, pnext):
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        self.name = text[:text.find('=')].strip()
        self.num = num
        self.next = pnext

    def print_class(self):
        print self.num ,self.next, self.name

def test_class_test_t():
    lala = test_t(10, 11)
    haha = test_t(12, 13)
    slow = test_t('slow', lala)
    rev = test_t('rev', haha)
    slow = slow.next
    slow.print_class()

    lala = test_t(10, 11)
    haha = test_t(12, 13)
    slow = test_t('slow', lala)
    rev = test_t('rev', haha)

    slow, slow.next, rev = slow.next, rev, slow
    slow.print_class()
    rev.print_class()

    lala = test_t(10, 11)
    haha = test_t(12, 13)
    slow = test_t('slow', lala)
    rev = test_t('rev', haha)

    rev, slow.next, slow = slow, rev, slow.next
    slow.print_class()
    rev.print_class()

def main():
    test_class_test_t()
    

if __name__ == "__main__":
    main()