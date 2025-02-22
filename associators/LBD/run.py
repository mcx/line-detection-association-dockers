# Copyright (c) 2023, Kirill Ivanov, Anastasiia Kornilova and Dmitrii Iarosh
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path

from adapter import Adapter
from common.parser import create_base_parser

if __name__ == "__main__":
    parser = create_base_parser(with_score_directory=False)
    args = parser.parse_args()

    Adapter(
        images_path=Path(args.imgs),
        lines_path=Path(args.lines),
        associations_dir=args.associations_dir,
        output_path=Path(args.output),
        frames_step=args.step,
        pairs_file=args.pairs,
    ).run()
