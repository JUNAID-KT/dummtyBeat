from dummybeat import BaseTest

import os


class Test(BaseTest):

    def test_base(self):
        """
        Basic test with exiting Dummybeat normally
        """
        self.render_config_template(
            path=os.path.abspath(self.working_dir) + "/log/*"
        )

        dummybeat_proc = self.start_beat()
        self.wait_until(lambda: self.log_contains("dummybeat is running"))
        exit_code = dummybeat_proc.kill_and_wait()
        assert exit_code == 0
